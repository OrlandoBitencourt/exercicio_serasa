from exercicio_serasa.services.orders.orders import *
from unittest import TestCase


class TestOrders(TestCase):
    def test_create_order_work(self):
        order_dict = dict(user_id=1,
                          item_description="fogao",
                          item_quantity=1,
                          item_price=5,
                          total_value=5)

        self.assertTrue(Orders().create_order(order_dict))

        self.assertFalse(Orders().create_order({}))

    def test_insert_order_work(self):
        pass

    def test_list_all_orders_work(self):
        pass

    def test_list_order_work(self):
        pass

    def test_list_order_by_user_work(self):
        pass

    def test_delete_order_work(self):
        pass

    def test_convert_user_data_work(self):
        pass

    def test_generate_data_orders_work(self):
        pass

    def test_calculate_total_work(self):
        pass
