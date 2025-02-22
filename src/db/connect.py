import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from src.main import app

load_dotenv()


# Configure the database URL from environment variables
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_size": 15,
    "max_overflow": 25,
    "pool_timeout": 86400,
    "pool_recycle": 1800,
    "pool_pre_ping": True,
}


# Initialize the database
db = SQLAlchemy(app)