from django.test import TestCase, Client
from main.models import Item

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')
    
    def setUp(self):
        return Item.objects.create(name = "Dimensity Destroyer", type = "Sword", atk = 2099, 
                                   rarity = "Gold", description = "blabla", amount = 1)
        
    def test_Item(self):
        DD = self.setUp()
        self.assertTrue(isinstance(DD, Item))
        self.assertEqual(DD.name, "Dimensity Destroyer")
        self.assertEqual(DD.type, "Sword")
        self.assertEqual(DD.atk, 2099)
        self.assertEqual(DD.rarity, "Gold")
        self.assertEqual(DD.amount, 1)