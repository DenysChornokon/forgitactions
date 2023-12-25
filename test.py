import unittest
import main as tested_app
import json

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        self.main = tested_app.app.test_client()

    def test_get_hello_endpoint(self):
        r = self.main.get('/')
        self.assertEqual(r._status_code, 200)
        self.assertEqual(r.get_data(), b'Hello world from app Pipeline testing.')


if __name__ == '__main__':
    unittest.main()
