from datetime import datetime
from functools import cache

import firebase_admin
from firebase_admin import firestore


def announcement_watcher(col_snapshot, changes, read_time):
    for change in changes:
        if change.type.name == 'ADDED':
            get_manager().add(change.document)
        elif change.type.name == 'MODIFIED':
            get_manager().modify(change.document)
        elif change.type.name == 'REMOVED':
            get_manager().remove(change.document)
    print('Updated announcements from callback...')


class DataManager:
    def __init__(self):
        print('Initializing announcements manager...')
        self.posts = {}
        self.last_post = 0
        self.last_update = 0
        self.app = firebase_admin.initialize_app(
            options={'projectId': 'rotr-app'})
        self.db = firestore.client()
        query = self.db.collection('announcements')
        print('Registering callback handler...')
        query.on_snapshot(announcement_watcher)

    def add(self, doc):
        self.posts[doc.id] = doc.to_dict()
        self.update_time()

    def modify(self, doc):
        self.add(doc)

    def remove(self, doc):
        del self.posts[doc.id]
        self.update_time()

    def update_time(self):
        self.last_post = max(map(int, self.posts.keys()))
        self.last_update = now()

    def save_post(self, *, user, subject, message):
        data = {'user': user, 'message': message, 'subject': subject}
        doc = self.db.collection('announcements').document(str(now()))
        doc.set(data)

    def validate_user(self, name, pw=''):
        doc = self.db.collection('users').document(name).get()
        doc_dict = doc.to_dict() if doc.exists else {}
        return doc_dict is not None and doc_dict.get('pet') == pw


@cache
def get_manager():
    return DataManager()


def now():
    return int(datetime.now().timestamp())
