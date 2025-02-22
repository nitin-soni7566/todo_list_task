from flask import request, jsonify
from flask_restful import Resource


class Home(Resource):
    def get(self):
        return jsonify({"message": "this is home route of todo list api"})
