from exercicio_serasa.services.db.security import *
from unittest import mock, TestCase


class TestSecurity(TestCase):
    def test_normalize_key_work(self):
        self.assertEqual((5, [7, 4, 4, 1, 2]), normalize_key("arroz"))

    @mock.patch("exercicio_serasa.services.db.security.normalize_key")
    def test_crypt_work(self, mock_normalize_key):
        mock_normalize_key.return_value = (5, [7, 4, 4, 1, 2])
        self.assertEqual("Àmmn9", crypt("arroz"))

    @mock.patch("exercicio_serasa.services.db.security.normalize_key")
    def test_uncrypt_work(self, mock_normalize_key):
        mock_normalize_key.return_value = (5, [7, 4, 4, 1, 2])
        self.assertEqual("arroz", uncrypt("Àmmn9"))
