from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Rule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rule_string = db.Column(db.Text, nullable=False)
    rule_ast = db.Column(db.JSON, nullable=False)

class UserData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, nullable=False)
    department = db.Column(db.String(50), nullable=False)
    salary = db.Column(db.Integer, nullable=False)
    experience = db.Column(db.Integer, nullable=False)

# Define the Node class for AST
class Node:
    def __init__(self, type, value, left=None, right=None):
        self.type = type
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node(type={self.type}, value={self.value})"
