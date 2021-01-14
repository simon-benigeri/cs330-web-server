import models
from flask import Response, request
from flask import Blueprint

api = Blueprint('comments', __name__)
@api.route('/api/comments/<post_id>/', methods=['GET', 'POST'])
def get_comments(post_id):
    if request.method == 'GET':
        data = models.Comment.objects(post=post_id).to_json()
        return Response(data, mimetype="application/json", status=200)
    else:
        return Response('POST method not handled yet.', mimetype="application/text", status=200)
