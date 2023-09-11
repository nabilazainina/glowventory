from django.test import TestCase, Client
from main.models import Items


class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    def test_show_main(self):
        # Untuk mendapat respon dari main
        response = Client().get('/main/')

        # Mengecek konten dari response context
        self.assertEqual(response.context['application_name'], 'glowventory')
        self.assertEqual(response.context['name'], 'Bella')
        self.assertEqual(response.context['class'], 'PBP C')

