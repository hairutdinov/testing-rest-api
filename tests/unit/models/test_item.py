from unittest import TestCase
from models.item import ItemModel


class TestItem(TestCase):
    def test_create_item(self):
        item = ItemModel('test', 100)
        self.assertEqual('test', item.name)
        self.assertEqual(100, item.price)

    def test_json(self):
        item = ItemModel('test', 100)
        expected = {
            'name': 'test',
            'price': 100,
        }
        self.assertDictEqual(expected, item.json())