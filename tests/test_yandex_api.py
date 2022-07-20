import unittest
from yandex_folder import create_folder


class TestFunctions(unittest.TestCase):

    def test_create_folder_copy(self):
        result = create_folder('World')
        etalon = 409
        self.assertEqual(result, etalon)

    def test_create_folder_new(self):
        result = create_folder('New_world')
        etalon = 201
        self.assertEqual(result, etalon)

    def test_not_found_resource(self):
        result = create_folder('Photo')
        etalon = 404
        self.assertNotEqual(result, etalon)

    def test_not_authorization(self):
        result = create_folder('New')
        etalon = 401
        self.assertNotEqual(result, etalon)