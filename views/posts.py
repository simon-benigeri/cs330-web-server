import models
from flask import Response, request
from flask import Blueprint
import json

api = Blueprint('posts', __name__)

@api.route('/api/posts/', methods=['GET', 'POST'])
def get_posts():
    if request.method == 'GET':
        # get list of all posts
        data = models.Post.objects.to_json()
        return Response(data, mimetype="application/json", status=200)
    else:
        # create a new post
        data = request.get_json()
        print(data)
        post = models.Post(**data).save()
        id = post.id
        response_text = json.dumps({'id': str(id)})
        return Response(response_text, mimetype="application/json", status=201)
