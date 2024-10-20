# Rule Engine Project Documentation

## Overview
This project is a simple 3-tier rule engine application that evaluates user eligibility based on attributes such as age, department, income, and experience. It uses an Abstract Syntax Tree (AST) to represent conditional rules and allows for dynamic creation, combination, and modification of these rules.

## Features
- Create rules from string expressions.
- Combine multiple rules into a single AST.
- Evaluate rules against user data.
- Error handling for invalid rules.

## Getting Started
- Clone the repository: `git clone <repository-url>`
- Install dependencies: `pip install -r requirements.txt`
- create an venv by: `python -m venv venv`
- Activate venv:`venv\Scripts\activate`
- Install some packages required:`>pip install flask flask-sqlalchemy`
- Run the application: `python app.py`
- To test the application:`python test_rule_evaluation.py`
- For error handling:`python test_error_handling.py`

## API Endpoints
- `/create_rule`: Create a rule and return its AST.
- `/combine_rules`: Combine multiple rules into a single AST.
- `/evaluate_rule`: Evaluate a rule against user data.

## License
This project is licensed under the MIT License.
