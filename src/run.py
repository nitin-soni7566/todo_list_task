from flask_restful import Api

from src.main import app
from src.routes.users import UserResource
from src.routes.todo import  TodoListResource, TodoResource
from src.routes.home import Home
from src.db.connect import db

api = Api(app)


# Add resources to the API
api.add_resource(Home, "/")
api.add_resource(UserResource, "/user")
api.add_resource(TodoListResource, "/todo")
api.add_resource(TodoResource, "/todo")


if __name__ == "__main__":
    with app.app_context():
        db.create_all() 
    app.run(debug=True)
