from flask import Blueprint, request, jsonify
from .rules import create_rule, combine_rules, evaluate_rule
from .models import Node  # Import Node class if you need it for AST representation

# Define the blueprint
app = Blueprint('api', __name__)

@app.route('/create_rule', methods=['POST'])
def create_rule_api():
    rule_string = request.json.get('rule')
    try:
        ast = create_rule(rule_string)
        return jsonify({'ast': ast.value})  # Return the value of the AST node
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@app.route('/combine_rules', methods=['POST'])
def combine_rules_api():
    rules = request.json.get('rules')
    if not rules:
        return jsonify({'error': 'No rules provided'}), 400
    try:
        combined_rule = combine_rules(rules)
        return jsonify({'combined_rule': combined_rule})  # Return the combined rule string
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_api():
    ast_data = request.json.get('ast')
    user_data = request.json.get('user_data')
    
    if not ast_data or not user_data:
        return jsonify({'error': 'AST data and user data are required'}), 400

    try:
        result = evaluate_rule(ast_data, user_data)
        return jsonify({'result': result})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    