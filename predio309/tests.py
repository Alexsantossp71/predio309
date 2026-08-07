"""Testes de fumaça do projeto Prédio 309 (Django)."""
from django.test import SimpleTestCase
from django.test import Client


class SmokeTests(SimpleTestCase):
    def setUp(self):
        self.client = Client()

    def test_admin_exige_login(self):
        """O /admin/ redireciona para o login (302) — app instalado e protegido."""
        response = self.client.get("/admin/")
        self.assertEqual(response.status_code, 302)
        self.assertIn("/admin/login/", response.url or "")

    def test_url_raiz_nao_existe_por_padrao(self):
        """Sem app configurado, a raiz retorna 404 (esperado no startproject)."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 404)

    def test_settings_secret_key_preenchida(self):
        """SECRET_KEY deve estar presente (de env ou fallback de dev)."""
        from django.conf import settings

        self.assertTrue(settings.SECRET_KEY)

    def test_settings_debug_booleano(self):
        """DEBUG deve ser um valor booleano válido vindo de DJANGO_DEBUG."""
        from django.conf import settings

        self.assertIsInstance(settings.DEBUG, bool)
