from unittest import TestCase
from models.item import ItemModel
from tests.unit.unit_base_test import UnitBaseTest


class TestItem(UnitBaseTest):
    def test_create_item(self):
        item = ItemModel('test', 100, 1)
        self.assertEqual('test', item.name)
        self.assertEqual(100, item.price)
        self.assertEqual(1, item.store_id)
        self.assertIsNone(item.store)

    def test_json(self):
        item = ItemModel('test', 100, 1)
        expected = {
            'name': 'test',
            'price': 100,
        }
        self.assertDictEqual(expected, item.json())