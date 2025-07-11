from django.test import TestCase
from django.urls import reverse, resolve
from .views import index  

class HomepageTest(TestCase):
    def setUp(self):
        """Ustawienia wspólne dla wszystkich testów"""
        self.url = reverse('index')

    def test_status_kodu_dla_slasha(self):
        """Strona główna powinna być dostępna pod '/'"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_status_kodu_dla_nazwy_sciezki(self):
        """Strona główna powinna być dostępna przez nazwę ścieżki 'index'"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_poprawny_szablon(self):
        """Powinien być użyty odpowiedni szablon: index.html"""
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'index.html')

    def test_zawartosc_strony(self):
        """Strona powinna zawierać oczekiwany tekst"""
        response = self.client.get(self.url)
        self.assertContains(response, "Welcome")  

    def test_brak_nieoczekiwanego_tekstu(self):
        """Strona nie powinna zawierać błędnych lub zbędnych informacji"""
        response = self.client.get(self.url)
        self.assertNotContains(response, "Error")

    def test_poprawne_przypisanie_funkcji_widoku(self):
        """Ścieżka '/' powinna być obsługiwana przez funkcję 'index'"""
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_404_dla_nieprawidlowej_sciezki(self):
        """Nieistniejąca ścieżka powinna zwracać błąd 404"""
        response = self.client.get('/nie-ma-takiej-strony/')
        self.assertEqual(response.status_code, 404)
