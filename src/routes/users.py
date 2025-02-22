import re
from flask import request, jsonify
from flask_restful import Resource, reqparse
from src.db.models import db, User


emailPattern = "([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"


def isEmailValid(email):
    match = re.fullmatch(emailPattern, email)
    if not match:
        return False
    return True


get_parser = reqparse.RequestParser()
get_parser.add_argument(
    "user_id", type=int, required=False, help="User id required", location="args"
)


# for new user
post_parser = reqparse.RequestParser()

post_parser.add_argument(
    "name", type=str, required=True, help="name required", location="args"
)
post_parser.add_argument(
    "email", type=str, required=True, help="email required", location="args"
)


class UserResource(Resource):
    def get(self):
        args = get_parser.parse_args()
        user_id = args["user_id"]
        if user_id:
            user = User.query.get(user_id)
            if not user:
                return {"error": "User not found"}, 404
            return jsonify({"id": user.id, "name": user.name, "email": user.email})
        else:
            users = User.query.all()
        return jsonify([{"id": u.id, "name": u.name, "email": u.email} for u in users])


    def post(self):
        args = post_parser.parse_args()
        email = args["email"]

        if isEmailValid(email):

            new_user = User(name=args["name"], email=email)
            db.session.add(new_user)
            db.session.commit()
            return {"message": "User created successfully"}, 201
        return {"message": "User give valid email"}, 500