import unittest
from main import CRUDApp


class FlaskCRUDTest(unittest.TestCase):
    def setUp(self):
        app = CRUDApp()
        self.app = app.app.test_client()

    def test_index(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Items", response.data)

    def test_add_item(self):
        response = self.app.post(
            "/add", data={"name": "New Item"}, follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("New Item", response.data.decode())

    def test_edit_item(self):
        response = self.app.post(
            "/edit/1", data={"name": "Updated Item"}, follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("Updated Item", response.data.decode())

    def test_delete_item(self):
        response = self.app.get("/delete/4", follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn("Item 1", response.data.decode())


if __name__ == "__main__":
    unittest.main()
