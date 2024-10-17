from datetime import datetime

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import reflex as rx

print('Initializing firebase...')
app = firebase_admin.initialize_app(options={'projectId': 'rotr-app'})
print('Acquiring firestore client...')
db = firestore.client()


class Announcement(rx.Base):
    time: int
    user: str
    message: str

    def __eq__(self, other):
        return self.time == other.time

    def __repr__(self):
        return f'({self.time}, {self.user}, {self.message})'


posts = []
updated = [0]


def wrap_post(fsdoc):
    data = fsdoc.to_dict()
    return Announcement(
        time=int(fsdoc.id),
        user=data.get('user'),
        message=data.get('message'))


def save_post(user, message):
    data = {'user': user, 'message': message}
    doc = db.collection('announcements').document(
        str(int(datetime.now().timestamp())))
    doc.set(data)


def on_snapshot(col_snapshot, changes, read_time):
    for change in changes:
        doc = wrap_post(change.document)
        if change.type.name == "ADDED":
            posts.append(doc)
        elif change.type.name == "MODIFIED":
            posts.remove(doc)
            posts.append(doc)
        elif change.type.name == "REMOVED":
            posts.remove(doc)
    posts.sort(key=lambda x: x.time, reverse=True)
    updated[0] = int(datetime.now().timestamp())
    print(f'Callback finished {updated[0]}')
    print(f'Updated announcements from callback...')


print('Creating announcements query...')
col_query = db.collection("announcements")

print('Registering announcements watcher...')
query_watch = col_query.on_snapshot(on_snapshot)


def validate_user(name, pw):
    doc = db.collection('users').document(name).get()
    return doc.exists and doc.to_dict().get('pet') == pw
