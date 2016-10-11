import unittest
import StringExtentions

exampleCamelCase="ToSnakeCase"
exampleSnakeCase="To_Camel_Case"

class TestStringExtentions(unittest.TestCase):
    def test_snakecase_to_camelcase(self):
        self.assertEqual(StringExtentions.SnakeCaseToCamelCase(exampleSnakeCase),"ToCamelCase")
    def test_camelcase_to_snakecase(self):
        self.assertEqual(StringExtentions.CamelCaseToSnakeCase(exampleCamelCase),"To_Snake_Case")

if __name__ == '__main__':
    unittest.main()
