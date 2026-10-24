import unittest
from app import app


class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_home_page(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)

    def test_home_page_message(self):
        response = self.client.get("/")

        self.assertIn(
            b"Hello! My Week 2 Docker application is running successfully.",
            response.data
        )


if __name__ == "__main__":
    unittest.main()