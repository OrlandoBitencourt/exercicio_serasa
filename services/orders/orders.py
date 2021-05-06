from bson import ObjectId
from exercicio_serasa.services.db.db import Database
from exercicio_serasa.services.db.security import uncrypt
import datetime


class Orders(Database):
    _id: str
    user_id: str
    item_description: str
    item_quantity: int
    item_price: float
    total_value: float
    created_at: str
    updated_at: str

    def __init__(self):
        super().__init__()

    def create_order(self, order_data: dict):
        try:
            self.user_id = order_data['user_id']
            self.item_description = order_data['item_description']
            self.item_quantity = order_data['item_quantity']
            self.item_price = order_data['item_price']
            self.total_value = order_data['total_value']
            return True
        except Exception as erro:
            print(str(erro))
            return False

    def insert_order(self) -> bool:
        try:
            self.orders.insert_one({'user_id': self.user_id,
                                    'item_description': self.item_description,
                                    'item_quantity': self.item_quantity,
                                    'item_price': self.item_price,
                                    'total_value': self.total_value,
                                    'created_at': str(datetime.datetime.now().strftime("%d-%m-%Y")),
                                    'updated_at': str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))})
            return True
        except Exception as erro:
            print(str(erro))
        return False

    def list_all_orders(self):
        return self.orders.find({})

    def list_order(self, order_id: str):
        return self.orders.find({'_id': ObjectId(order_id)})

    def list_order_by_user(self, user_id: str):
        return self.orders.find({'user_id': user_id})

    def delete_order(self, order_id: str) -> bool:
        try:
            db_data = self.list_order(order_id)
            order_to_delete = self.generate_data_orders(db_data)
            order_to_delete['id'] = ObjectId(order_to_delete['id'])
        except Exception as erro:
            print(str(erro))
            return False
        self.orders.delete_one({"_id": order_to_delete['id']})
        return True

    def update_order(self, order_id: str, new_order_data: dict) -> bool:
        db_data = self.list_order(order_id)
        old_order_data = self.generate_data_orders(db_data)

        new_order_data['created_at'] = old_order_data['created_at']
        new_order_data['updated_at'] = str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

        self.orders.update_one({"_id": ObjectId(old_order_data['id'])}, {"$set": new_order_data})
        return True

    def convert_user_data(self, user_data: dict) -> dict:
        new_user_data = {'id': str(user_data['id']),
                         'name': uncrypt(user_data['name']),
                         'cpf': uncrypt(user_data['cpf']),
                         'email': uncrypt(user_data['email']),
                         'phone_number': uncrypt(user_data['phone_number']),
                         'created_at': user_data['created_at'],
                         'updated_at': user_data['updated_at']}
        return new_user_data

    def generate_data_orders(self, order_data: list) -> dict:
        for order in order_data:
            order_dict = ({'id': order['_id'],
                           'user_id': order['user_id'],
                           'item_description': order['item_description'],
                           'item_quantity': order['item_quantity'],
                           'item_price': order['item_price'],
                           'total_value': order['total_value'],
                           'created_at': order['created_at'],
                           'updated_at': order['updated_at']})
            return order_dict

    def calculate_total(self, qtd: int, price: float) -> float:
        return qtd * price


# order_1 = Orders()
# original_data = {'id': "6092cbc4f9dfc0891202e223",
#                          'name': "Fka;g69ãã9.ANía / eJWNn ",
#                          'cpf': "0ü0õUÉõÉhõP",
#                          'email': "oklÀ7cX@H5làHXgBC",
#                          'phone_number': "4À9GJQGaGGJ",
#                          'created_at': "05-05-2021",
#                          'updated_at': "05-05-2021 13:45:56"}
# print(order_1.convert_user_data(original_data))