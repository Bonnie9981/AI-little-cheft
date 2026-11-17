import importlib.util
import unittest

spec = importlib.util.spec_from_file_location("validate_recipes", "scripts/validate_recipes.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class RecipeDatasetTests(unittest.TestCase):
    def test_dataset_integrity(self):
        self.assertEqual(module.validate(), 0)

if __name__ == "__main__":
    unittest.main()
