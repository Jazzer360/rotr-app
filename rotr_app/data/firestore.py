from datetime import datetime
from functools import cache

import firebase_admin
from firebase_admin import firestore

from ..util.utils import no_compile


@no_compile((None, None))
@cache
def get_client():
    print('Initializing firebase client...')
    app = firebase_admin.initialize_app(options={'projectId': 'rotr-app'})
    return app, firestore.client()


app, db = get_client()


def announcement_watcher(col_snapshot, changes, read_time):
    for change in changes:
        if change.type.name == "ADDED":
            manager.add(change.document)
        elif change.type.name == "MODIFIED":
            manager.modify(change.document)
        elif change.type.name == "REMOVED":
            manager.remove(change.document)
    print('Updated announcements from callback...')


class AnnouncementManager:
    def __init__(self):
        print('Initializing announcements manager...')
        self.posts = {}
        self.last_post = 0
        if db:
            query = db.collection('announcements')
            print('Registering callback handler...')
            query.on_snapshot(announcement_watcher)

    def add(self, doc):
        self.posts[doc.id] = doc.to_dict()
        self.update_time()

    def modify(self, doc):
        self.add(doc)

    def remove(self, doc):
        del self.posts[doc.id]

    def update_time(self):
        self.last_post = now()


manager = AnnouncementManager()


def save_post(*, user, subject, message):
    data = {'user': user, 'message': message, 'subject': subject}
    doc = db.collection('announcements').document(str(now()))
    doc.set(data)


def validate_user(name, pw):
    doc = db.collection('users').document(name).get()
    return doc.exists and doc.to_dict().get('pet') == pw


def now():
    return int(datetime.now().timestamp())
