import unittest
from unittest import TestCase
from fastapi.testclient import TestClient
from unit_converter.main import app

# we will not be overriding the get_body() dependency. since we are trying to test the form-parsing behavior
# for unit tests we always want to override dependecies which access external databases or call third party apis to avoid relying on those external systems during testing
# For integration tests, we might deliberately use a test database.
class TestApp(TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_get_home_page_renders_layouts_html(self):
        resp = self.client.get("/")
        # a FastApi response header object is nt a standard Python dict it is a dictionary-like mapping object meaning it implements the standard mapping interface
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.headers.get("content-type"), "text/html; charset=utf-8")
        self.assertIn("<h1>Unit Converter</h1>", resp.text)
        self.assertEqual(resp.template.name, "layouts.html")

    def test_get_length_route_renders_length_html(self):
        resp = self.client.get("/length")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.headers.get("content-type"), "text/html; charset=utf-8")
        self.assertIn("Enter the length to convert", resp.text)
        self.assertEqual(resp.template.name, "length.html")
        self.assertEqual(resp.context.get("title"), "length")
        # assertIs() checks object identity rather than equality, so it verifies that the value is exactly False. This to avoid the case where converted is 0 because python considers False == 0  # True 
        self.assertIs(resp.context.get("converted"), False)

    def test_get_temperature_route_renders_temperature_html(self):
        resp = self.client.get("/temperature")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.headers.get("content-type"), "text/html; charset=utf-8")
        self.assertIn("Enter the temperature to convert", resp.text)
        self.assertEqual(resp.template.name, "temperature.html")
        self.assertEqual(resp.context.get("title"), "temperature")
        self.assertIs(resp.context.get("converted"), False)

    def test_get_weight_route_renders_weight_html(self):
        resp = self.client.get("/weight")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.headers.get("content-type"), "text/html; charset=utf-8")
        self.assertIn("Enter the weight to convert", resp.text)
        self.assertEqual(resp.template.name, "weight.html")
        self.assertEqual(resp.context.get("title"), "weight")
        self.assertIs(resp.context.get("converted"), False)


if __name__ == "__main__":
    unittest.main()
