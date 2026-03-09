from django.test import TestCase


class BasicTests(TestCase):

    def test_admin_login_page(self):
        response = self.client.get("/admin/login/")
        self.assertEqual(response.status_code, 200)

    def test_admin_redirect(self):
        response = self.client.get("/admin/")
        self.assertEqual(response.status_code, 302)

    def test_invalid_page(self):
        response = self.client.get("/invalid-url/")
        self.assertEqual(response.status_code, 404)

    def test_admin_logout_redirect(self):
        response = self.client.get("/admin/logout/")
        self.assertIn(response.status_code, [200, 302])

    def test_admin_password_reset(self):
        response = self.client.get("/admin/password_reset/")
        self.assertIn(response.status_code, [200, 302])
        