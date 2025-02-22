from flask import request, jsonify
from flask_restful import Resource,reqparse
from src.db.models import db, Todo,User


get_parser = reqparse.RequestParser()

get_parser.add_argument(
    "user_id", type=int, required=False, help="User id required", location="args"
)
get_parser.add_argument(
    "todo_id", type=int, required=False, help="todo_id id required", location="args"
)


# for new user
post_parser = reqparse.RequestParser()

post_parser.add_argument(
    "title", type=str, required=True, help="title required", location="args"
)
post_parser.add_argument(
    "user_id", type=int, required=True, help="user_id required", location="args"
)


class TodoListResource(Resource):
    def get(self):
        args = get_parser.parse_args()
        user_id = args["user_id"]
        todos = Todo.query.filter_by(user_id=user_id).all()
        return jsonify([{"id": t.id, "title": t.title} for t in todos])

    def post(self):
        args = post_parser.parse_args()
        user_id = args["user_id"]
        user = User.query.get(user_id)
        if not user:
            return {"error": "User not found"}, 404

        new_todo = Todo(title=args["title"], user_id=user.id)
        db.session.add(new_todo)
        db.session.commit()
        return {"message": "Task created successfully"}, 201


class TodoResource(Resource):
    def delete(self):
        args = get_parser.parse_args()
        todo_id = args["todo_id"]
        todo = Todo.query.get(todo_id)
        if not todo:
            return {"error": "Task not found"}, 404

        db.session.delete(todo)
        db.session.commit()
        return {"message": "Task deleted successfully"}, 200
