from bson import ObjectId
from db.db import Database
from db.security import crypt
import datetime


class Users(Database):
    _id: str
    name: str
    cpf: str
    email: str
    phone_number: int
    created_at: str
    updated_at: str

    def __init__(self):
        super().__init__()

    def create_user(self, user_data: dict):
        try:
            self.name = crypt(user_data["name"])
            self.cpf = crypt(user_data["cpf"])
            self.email = crypt(user_data["email"])
            self.phone_number = crypt(user_data["phone_number"])
            return True
        except Exception as erro:
            print(str(erro))
            return False

    def insert_user(self) -> bool:
        try:
            self.users.insert_one({'name': self.name,
                                   'cpf': self.cpf,
                                   'email': self.email,
                                   'phone_number': self.phone_number,
                                   'created_at': str(datetime.datetime.now().strftime("%d-%m-%Y")),
                                   'updated_at': str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))})
            return True
        except Exception as erro:
            print(str(erro))
        return False

    def list_all_users(self):
        return self.users.find({})

    def list_user(self, cpf: str):
        return self.users.find({'cpf': crypt(cpf)})

    def delete_user(self, cpf: str) -> bool:
        try:
            db_data = self.list_user(cpf)
            user_to_delete = self.generate_data_users(db_data)
            user_to_delete['id'] = ObjectId(user_to_delete['id'])
            self.users.delete_one({"_id": user_to_delete['id']})
        except Exception as erro:
            print(str(erro))
            return False
        return True

    def update_user(self, cpf: str, new_user_data: dict) -> bool:
        db_data = self.list_user(cpf)
        old_user_data = self.generate_data_users(db_data)

        new_user_data = self.convert_user_data(new_user_data)
        new_user_data['_id'] = ObjectId(old_user_data['id'])
        new_user_data['created_at'] = old_user_data['created_at']
        new_user_data['updated_at'] = str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

        self.users.update_one({"_id": new_user_data['_id']}, {"$set": new_user_data})
        return True

    def convert_user_data(self, user_data: dict) -> dict:
        new_user_data = {'name': crypt(user_data['name']), 'cpf': crypt(user_data['cpf']),
                         'email': crypt(user_data['email']), 'phone_number': crypt(user_data['phone_number'])}
        return new_user_data

    def generate_data_users(self, user_data: list) -> dict:
        for user in user_data:
            user_dict = ({'id': str(user['_id']),
                          'name': user['name'],
                          'cpf': user['cpf'],
                          'email': user['email'],
                          'phone_number': user['phone_number'],
                          'created_at': user['created_at'],
                          'updated_at': user['updated_at']})
            return user_dict
