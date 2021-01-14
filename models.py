import datetime
from mongoengine import \
    Document, StringField, DateTimeField, ReferenceField, CASCADE

class Post(Document):
    title = StringField(required=True, max_length=200)
    content = StringField(required=True)
    author = StringField(required=True, max_length=50)
    published = DateTimeField(default=datetime.datetime.now)

class Comment(Document):
    comment = StringField(required=True)
    author = StringField(required=True, max_length=50)
    post = ReferenceField('Post', reverse_delete_rule=CASCADE)