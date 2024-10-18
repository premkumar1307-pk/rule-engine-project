import unittest
from app.rules import create_rule, evaluate_rule, validate_attributes, evaluate_condition, RuleEngineError

class TestRuleEngineErrorHandling(unittest.TestCase):

    def test_missing_attribute(self):
        with self.assertRaises(RuleEngineError) as context:
            validate_attributes({"age": 25, "salary": 50000})  # Missing department and experience
        self.assertEqual(str(context.exception), "Missing required attribute: department")

    def test_invalid_attribute_type(self):
        with self.assertRaises(RuleEngineError) as context:
            validate_attributes({"age": "twenty-five", "department": "Marketing", "salary": 50000, "experience": 2})
        self.assertEqual(str(context.exception), "Invalid type for age: expected int, got str")

    def test_invalid_attribute_value(self):
        with self.assertRaises(RuleEngineError) as context:
            validate_attributes({"age": -5, "department": "Marketing", "salary": 50000, "experience": 2})
        self.assertEqual(str(context.exception), "Invalid value for age: -5")

    def test_unknown_rule(self):
        with self.assertRaises(RuleEngineError) as context:
            create_rule("unknown rule")
        self.assertEqual(str(context.exception), "Unknown rule: unknown rule")

    def test_unknown_condition(self):
        with self.assertRaises(RuleEngineError) as context:
            evaluate_condition({"age": 30, "department": "Sales", "salary": 60000, "experience": 5}, "unknown condition")
        self.assertEqual(str(context.exception), "Unknown condition: unknown condition")

if __name__ == "__main__":
    unittest.main()
