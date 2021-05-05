from exercicio_serasa.services.db.response import *
from unittest import TestCase


class TestResponse(TestCase):
    def test_gera_response_work(self):
        self.assertEqual("<Response 31 bytes [200 OK]>", str(gera_response(200, "teste", {}, "ok")))
