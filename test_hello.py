import unittest
from app import app

class TestHelloWorld(unittest.TestCase):
    def setUp(self):
        # Creates a test client for the Flask application
        self.client = app.test_client()
        self.client.testing = True

    def test_hello_world(self):
        # Sends a GET request to the root URL
        response = self.client.get('/')
        # Asserts that the status code is 200
        self.assertEqual(response.status_code, 200)
        # Asserts that the response data contains 'Hello, World!'
        self.assertIn(b'Hello, World!', response.data)

if __name__ == '__main__':
    unittest.main()
