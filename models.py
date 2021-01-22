import datetime
import json

from mongoengine import \
    Document, StringField, DateTimeField, ReferenceField, ListField, CASCADE

class Post(Document):
    title = StringField(required=True, max_length=200)
    content = StringField(required=True)
    author = StringField(required=True, max_length=50)
    published = DateTimeField(default=datetime.datetime.now)

    def to_dict(self, path=None):
        url = "/api/posts/" + str(self.pk) + "/"
        if path:
            url = path + url
        return {
            "id": str(self.pk),
            "title": self.title,
            "content": self.content,
            "author": self.author,
            "published": self.published.isoformat(),
            "url": url
        }

    def to_json(self, path=None):
        return json.dumps(self.to_dict(path=path))

class Comment(Document):
    comment = StringField(required=True)
    author = StringField(required=True, max_length=50)
    post = ReferenceField('Post', reverse_delete_rule=CASCADE)

    def to_dict(self, path=None):
        d = {
            "id": str(self.pk),
            "comment": self.comment,
            "author": self.author,
            "post_id": str(self.post.pk)
        }
        if path:
            server_url = path + str(self.pk) + '/'
            d.update({
                'url': server_url
            })
        return d
    
    def to_json(self, path=None):
        return json.dumps(self.to_dict())

# from .db import db

# class Movie(Document):
#     name = StringField(required=True, unique=True)
#     casts = ListField(StringField(), required=True)
#     genres =ListField(StringField(), required=True)
        