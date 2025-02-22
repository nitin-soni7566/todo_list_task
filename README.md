# **📉 Todo List API**  

A simple **Flask-RESTful API** for managing a to-do list.

## **🚀 Features**  
- Create, read, and delete (CRUD) tasks  And add user, get user 
- Uses **Flask, Flask-RESTful, Flask-SQLAlchemy**  
- No authentication required (open API)  

## **📛 Installation**  

1. **Create a virtual environment**  
```sh
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
```

2. **Install dependencies**  
```sh
pip install poetry

poetry install
```


3. **Run the application**  
```sh
pythom -m src.run
```

---

## **🛠 API Endpoints**  

| Method | Endpoint        | Description          | Example |
|--------|----------------|----------------------|---------|
| **GET** | `/user`        | Get all user       | `GET /user` |
| **GET** | `/user?user_id=<int:id>`   | Get a single user   | `GET /user/?user_id=1` |
| **POST** | `/user`       | Add a new user   | `POST /user?name=nitin soni&email=test@gmail.com` |
| **GET** | `/todo?user_id=<int:id>`   | Get user task   | `GET todo?user_id=1` |
| **POST** | `/todo`       | Create a new task   | `POST /todos?user_id=1&title=have to complete task ` |
| **DELETE** | `/todos?todo_id=<int:id>` | Delete a task       | `DELETE /todo?todo_id=1` |


## **📌 Notes**  
- This API does **not** require authentication.  
- I have added a Thunder Client collection for this to-do list API.
- task_1.py file is for task one.
- task_2.py file is for task two.
- src directory contains the to-do API. 
---