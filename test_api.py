import requests

def test_create_rule(rule):
    url = "http://127.0.0.1:5000/api/create_rule"
    data = {"rule": rule}
    response = requests.post(url, json=data)
    print(f"Create Rule Response: {response.json()}")

def test_combine_rules(rules):
    url = "http://127.0.0.1:5000/api/combine_rules"
    data = {"rules": rules}
    response = requests.post(url, json=data)
    print(f"Combine Rules Response: {response.json()}")

def test_evaluate_rule(ast, user_data):
    url = "http://127.0.0.1:5000/api/evaluate_rule"
    data = {
        "ast": ast,
        "data": user_data
    }
    response = requests.post(url, json=data)
    print(f"Evaluate Rule Response: {response.json()}")

if __name__ == "__main__":
    # Test the new rules
    test_create_rule("age > 30 AND department == 'Sales'")
    test_create_rule("((age < 40 AND department = 'Engineering') OR (income > 80000 AND spend < 1000))")
    test_create_rule("(age > 30 AND department = 'HR') OR (salary < 30000 AND experience < 2)")
    test_create_rule("(spend > 1500 OR experience > 10) AND (department = 'Sales')")
    
    # Test combining rules
    test_combine_rules([
        "age > 30 AND department == 'Sales'",
        "age < 40 AND department = 'Engineering'",
        "(age > 30 AND department = 'HR') OR (salary < 30000 AND experience < 2)"
    ])

    # Test evaluating a rule
    user_data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3, "income": 90000, "spend": 500}
    test_evaluate_rule("age > 30", user_data)
