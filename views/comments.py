from flask import Response, request
from flask_restful import Resource
from mongoengine import DoesNotExist, Q
import models
import json

class CommentListEndpoint(Resource):
    
    def get(self):
        # TODO: implement GET endpoint
        return Response(json.dumps([]), mimetype="application/json", status=200)

    def post(self):
        # TODO: implement POST endpoint
        return Response(json.dumps([]), mimetype="application/json", status=201)
        
class CommentDetailEndpoint(Resource):
    def put(self, id):
        # TODO: implement PUT endpoint
        return Response(json.dumps([]), mimetype="application/json", status=200)
    
    def delete(self, id):
        # TODO: implement DELETE endpoint
        return Response(json.dumps([]), mimetype="application/json", status=200)

    def get(self, id):
        # TODO: implement GET endpoint
        return Response(json.dumps([]), mimetype="application/json", status=200)

def initialize_routes(api):
    api.add_resource(CommentListEndpoint, '/api/comments', '/api/comments/')
    api.add_resource(CommentDetailEndpoint, '/api/comments/<id>', '/api/comments/<id>/')
    # api.add_resource(CommentListEndpoint, '/api/posts/<post_id>/comments', '/api/posts/<post_id>/comments/')
    # api.add_resource(CommentDetailEndpoint, '/api/posts/<post_id>/comments/<id>', '/api/posts/<post_id>/comments/<id>/')