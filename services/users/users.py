from exercicio_serasa.services.db.db import Database
from exercicio_serasa.services.db.security import crypt


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
            self.created_at = user_data["created_at"]
            self.updated_at = user_data["updated_at"]
            return True
        except:
            return False

    def insert_user(self) -> bool:
        try:
            self.users.insert_one({'name': self.name,
                                   'cpf': self.cpf,
                                   'email': self.email,
                                   'phone_number': self.phone_number,
                                   'created_at': self.created_at,
                                   'updated_at': self.updated_at})
            return True
        except Exception as erro:
            print(str(erro), str(erro.args))
        return False

    def list_all_users(self):
        return self.users.find({})

    def list_user(self, cpf: str):
        return self.users.find({'cpf': crypt(cpf)})

    def update_user(self, user_data: dict) -> bool:
        pass

    def delete_user(self, cpf: str) -> bool:
        pass