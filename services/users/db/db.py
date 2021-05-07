import pymongo


class Database():
    def __init__(self):
        self.conn = pymongo.MongoClient("mongodb://mongodb:27017/")
        self.db = self.conn['serasa']
        self.users = self.db['users']
        self.orders = self.db['orders']
