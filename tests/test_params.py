import unittest
from app.helpers.utils import newfile_parameters

class TestNewFileParams(unittest.TestCase):
    def test_params(self):
        wrongparams = {
            "titulo":"blabla",
            "descrip": "bleble"
        }
        rightparams = {
            "titulo":"blabla",
            "descripcion": "bleble"
        }
        converted = {
            "name":"blabla",
            "description": "bleble"
        }
        self.assertEqual(newfile_parameters(wrongparams), False)
        self.assertEqual(newfile_parameters(rightparams), converted)

if __name__ == "__main__":
    unittest.main()