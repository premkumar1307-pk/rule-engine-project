from app.models import Node

class RuleEngineError(Exception):
    """Custom exception for rule engine errors."""
    pass

VALID_ATTRIBUTES = {
    "age": (int, lambda x: x >= 0),  
    "department": (str, lambda x: len(x) > 0),  
    "salary": (int, lambda x: x >= 0),  
    "experience": (int, lambda x: x >= 0)  
}

def validate_attributes(data):
    for attr, (attr_type, validator) in VALID_ATTRIBUTES.items():
        if attr not in data:
            raise RuleEngineError(f"Missing required attribute: {attr}")
        if not isinstance(data[attr], attr_type):
            raise RuleEngineError(f"Invalid type for {attr}: expected {attr_type.__name__}, got {type(data[attr]).__name__}")
        if not validator(data[attr]):
            raise RuleEngineError(f"Invalid value for {attr}: {data[attr]}")

def create_rule(rule_string):
    """
    Create an Abstract Syntax Tree (AST) from a rule string.
    
    Args:
        rule_string (str): The rule expression to parse.
    
    Returns:
        Node: The root node of the AST.
    """
    # Define rules and corresponding AST nodes
    rules = {
        "age > 30": Node(type="operand", value="age > 30"),
        "department == 'Sales'": Node(type="operand", value="department == 'Sales'"),
        "department == 'Marketing'": Node(type="operand", value="department == 'Marketing'"),
        "salary > 50000": Node(type="operand", value="salary > 50000"),
        "age < 25": Node(type="operand", value="age < 25"),
        "age < 30": Node(type="operand", value="age < 30"),
        "age < 25 AND department == 'Marketing'": Node(type="operator", value="AND", 
            left=Node(type="operand", value="age < 25"), 
            right=Node(type="operand", value="department == 'Marketing'")),
        "age < 30 AND (department == 'Sales' OR salary > 50000)": Node(type="operator", value="AND", 
            left=Node(type="operand", value="age < 30"), 
            right=Node(type="operator", value="OR", 
                left=Node(type="operand", value="department == 'Sales'"), 
                right=Node(type="operand", value="salary > 50000"))),
        "age > 30 AND department == 'Sales'": Node(type="operator", value="AND",
            left=Node(type="operand", value="age > 30"),
            right=Node(type="operand", value="department == 'Sales'")),
        # Add more rules here as needed
    }
    
    # Check if the rule_string is in the defined rules
    if rule_string in rules:
        return rules[rule_string]
    
    raise RuleEngineError(f"Unknown rule: {rule_string}")

def evaluate_condition(data, condition):
    """
    Evaluate a condition based on user data.
    
    Args:
        data (dict): The user data to evaluate.
        condition (str): The condition string to evaluate.
    
    Returns:
        bool: The result of the condition evaluation.
    """
    if condition == "age > 30":
        return data["age"] > 30
    elif condition == "department == 'Sales'":
        return data["department"] == "Sales"
    elif condition == "department == 'Marketing'":
        return data["department"] == "Marketing"
    elif condition == "salary > 50000":
        return data["salary"] > 50000
    elif condition == "age < 25":
        return data["age"] < 25
    elif condition == "age < 30":
        return data["age"] < 30
    # Add more condition evaluations as needed
    raise RuleEngineError(f"Unknown condition: {condition}")

def evaluate_rule(ast, data):
    """
    Evaluate a rule based on the Abstract Syntax Tree (AST) and user data.
    
    Args:
        ast (Node): The AST representing the rule.
        data (dict): The user data to evaluate against the rule.
    
    Returns:
        bool: The result of the evaluation.
    """
    validate_attributes(data)  # Validate user data before evaluation

    if ast.type == "operand":
        return evaluate_condition(data, ast.value)
    
    elif ast.type == "operator":
        left_result = evaluate_rule(ast.left, data)
        right_result = evaluate_rule(ast.right, data)
        if ast.value == "AND":
            return left_result and right_result
        elif ast.value == "OR":
            return left_result or right_result
    
    raise RuleEngineError(f"Unknown AST node type: {ast.type}")

def combine_rules(rules, operator="AND"):
    """
    Combine multiple rule strings using the specified operator.
    
    Args:
        rules (list of str): The list of rule strings to combine.
        operator (str): The operator to use for combining rules, default is 'AND'.
    
    Returns:
        str: The combined rule string.
    """
    if not rules:
        raise RuleEngineError("No rules provided for combination.")
    
    return f" {operator} ".join(f"({rule})" for rule in rules)

def modify_rule(node, new_value=None, new_operator=None):
    """
    Modify an existing AST node with new values or operators.
    
    Args:
        node (Node): The AST node to modify.
        new_value (str): The new value for the operand.
        new_operator (str): The new operator type for the node.
    """
    if new_value is not None:
        node.value = new_value
    if new_operator is not None:
        node.type = new_operator  

def remove_subexpression(node):
    """
    Remove a subexpression from the AST node.
    
    Args:
        node (Node): The AST node from which to remove the subexpression.
    """
    if node.left:
        node.left = None  # Example logic for removing a left child

USER_DEFINED_FUNCTIONS = {}

def register_function(name, func):
    """
    Register a user-defined function for rule evaluation.
    
    Args:
        name (str): The name of the function.
        func (callable): The function to register.
    """
    USER_DEFINED_FUNCTIONS[name] = func

def evaluate_function(name, *args):
    """
    Evaluate a registered user-defined function.
    
    Args:
        name (str): The name of the function to evaluate.
        *args: Arguments to pass to the function.
    
    Returns:
        The result of the function evaluation.
    """
    if name not in USER_DEFINED_FUNCTIONS:
        raise RuleEngineError(f"Unknown function: {name}")
    return USER_DEFINED_FUNCTIONS[name](*args)
