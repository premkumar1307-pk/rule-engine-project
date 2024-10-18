from app.rules import create_rule, evaluate_rule

def test_rule_evaluation():
    test_cases = [
        {
            "rule": "age < 25 AND department == 'Marketing'",
            "user_data": {"age": 22, "department": "Marketing", "salary": 30000, "experience": 2},
            "expected_result": True
        },
        {
            "rule": "age < 25 AND department == 'Marketing'",
            "user_data": {"age": 26, "department": "Marketing", "salary": 40000, "experience": 3},
            "expected_result": False
        },
        {
            "rule": "age > 30 AND department == 'Sales'",
            "user_data": {"age": 31, "department": "Sales", "salary": 60000, "experience": 5},
            "expected_result": True
        },
        {
            "rule": "salary > 50000",
            "user_data": {"age": 22, "department": "Marketing", "salary": 30000, "experience": 2},
            "expected_result": False
        },
        {
            "rule": "age < 30 AND (department == 'Sales' OR salary > 50000)",
            "user_data": {"age": 28, "department": "Sales", "salary": 40000, "experience": 4},
            "expected_result": True
        },
        {
            "rule": "age < 30 AND (department == 'Sales' OR salary > 50000)",
            "user_data": {"age": 31, "department": "Marketing", "salary": 20000, "experience": 1},
            "expected_result": False
        },
    ]

    for case in test_cases:
        rule_string = case["rule"]
        user_data = case["user_data"]
        expected_result = case["expected_result"]

        ast = create_rule(rule_string)
        result = evaluate_rule(ast, user_data)

        print(f"Evaluating rule '{rule_string}' with user data {user_data}: {result}")
        assert result == expected_result, f"Failed for rule: {rule_string} with data: {user_data}"

if __name__ == "__main__":
    test_rule_evaluation()