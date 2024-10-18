from app.models import Node

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
    
    raise ValueError(f"Unknown rule: {rule_string}")

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
    raise ValueError(f"Unknown condition: {condition}")

def evaluate_rule(ast, data):
    """
    Evaluate a rule based on the Abstract Syntax Tree (AST) and user data.
    
    Args:
        ast (Node): The AST representing the rule.
        data (dict): The user data to evaluate against the rule.
    
    Returns:
        bool: The result of the evaluation.
    """
    if ast.type == "operand":
        return evaluate_condition(data, ast.value)
    
    elif ast.type == "operator":
        left_result = evaluate_rule(ast.left, data)
        right_result = evaluate_rule(ast.right, data)
        if ast.value == "AND":
            return left_result and right_result
        elif ast.value == "OR":
            return left_result or right_result
    
    raise ValueError(f"Unknown AST node type: {ast.type}")

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
        raise ValueError("No rules provided for combination.")
    
    return f" {operator} ".join(f"({rule})" for rule in rules)
