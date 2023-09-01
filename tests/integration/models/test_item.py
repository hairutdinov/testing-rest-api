from models.item import ItemModel
from tests.base_test import BaseTest
from models.store import StoreModel


class ItemTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            StoreModel('test').save_to_db()
            item = ItemModel('test', 100, 1)
            self.assertIsNone(ItemModel.find_by_name('test'))
            item.save_to_db()
            self.assertIsNotNone(ItemModel.find_by_name('test'))
            item.delete_from_db()
            self.assertIsNone(ItemModel.find_by_name('test'))
