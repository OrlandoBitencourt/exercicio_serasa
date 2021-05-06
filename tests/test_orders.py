from exercicio_serasa.services.orders.orders import *
from unittest import TestCase, mock


class TestOrders(TestCase):
    def test_create_order_work(self):
        order_dict = dict(user_id=1,
                          item_description="fogao",
                          item_quantity=1,
                          item_price=5,
                          total_value=5)

        self.assertTrue(Orders().create_order(order_dict))

        self.assertFalse(Orders().create_order({}))

    @mock.patch("exercicio_serasa.services.orders.orders.Orders.orders", create=True)
    def test_insert_order_work(self, mock_orders):
        order_test = Orders()

        self.assertFalse(order_test.insert_order())

        order_dict = dict(user_id="6092cbc4f9dfc0891202e223",
                          item_description="fogao",
                          item_quantity=1,
                          item_price=5,
                          total_value=5)

        order_test.user_id = order_dict['user_id']
        order_test.item_description = order_dict['item_description']
        order_test.item_quantity = order_dict['item_quantity']
        order_test.item_price = order_dict['item_price']
        order_test.total_value = order_dict['total_value']

        self.assertTrue(order_test.insert_order())

    @mock.patch("exercicio_serasa.services.orders.orders.Orders.orders", create=True)
    def test_list_all_orders_work(self, mock_orders):
        order_test = Orders()
        mock_orders.find.return_value = True
        self.assertTrue(order_test.list_all_orders())

    @mock.patch("exercicio_serasa.services.orders.orders.Orders.orders", create=True)
    def test_list_order_work(self, mock_orders):
        order_test = Orders()
        mock_orders.find.return_value = True
        self.assertTrue(order_test.list_order("6092cbc4f9dfc0891202e223"))

    @mock.patch("exercicio_serasa.services.orders.orders.Orders.orders", create=True)
    def test_list_order_by_user_work(self, mock_orders):
        order_test = Orders()
        mock_orders.find.return_value = True
        self.assertTrue(order_test.list_order_by_user("666"))

    @mock.patch("exercicio_serasa.services.orders.orders.Orders.orders", create=True)
    def test_delete_order_work(self, mock_orders):
        order_test = Orders()

        self.assertFalse(order_test.delete_order("6092cbc4f9dfc0891202e223"))

        db_order_dict = dict(user_id="6092cbc4f9dfc0891202e223",
                          item_description="fogao",
                          item_quantity=1,
                          item_price=5,
                          total_value=5,
                          created_at="",
                          updated_at="")
        db_order_dict["_id"] = "6092cbc4f9dfc0891202e223"

        generated_order_dict = dict(id="6092cbc4f9dfc0891202e223",
                          user_id="6092cbc4f9dfc0891202e223",
                          item_description="fogao",
                          item_quantity=1,
                          item_price=5,
                          total_value=5,
                          created_at="",
                          updated_at="")

        mock_orders.list_order.return_value = db_order_dict
        mock_orders.generate_data_orders.return_value = generated_order_dict

        self.assertTrue(order_test.delete_order(order_id="609412a51a55b3834ed7c35a"))

    def test_convert_user_data_work(self):
        order_test = Orders()

        original_data = {'id': "6092cbc4f9dfc0891202e223",
                         'name': "Fka;g69ãã9.ANía / eJWNn ",
                         'cpf': "0ü0õUÉõÉhõP",
                         'email': "oklÀ7cX@H5làHXgBC",
                         'phone_number': "4À9GJQGaGGJ",
                         'created_at': "05-05-2021",
                         'updated_at': "05-05-2021 13:45:56"}

        converted_data = {'id': '6092cbc4f9dfc0891202e223',
                          'name': 'Francielle Karolyne Mann',
                          'cpf': '00000000001',
                          'email': 'orlando@gmail.com',
                          'phone_number': '47999999599',
                          'created_at': '05-05-2021',
                          'updated_at': '05-05-2021 13:45:56'}

        self.assertEqual(converted_data, order_test.convert_user_data(original_data))

    def test_generate_data_orders_work(self):
        pass

    def test_calculate_total_work(self):
        order_test = Orders()
        self.assertEqual(1.0, order_test.calculate_total(1, 1.0))
