from exercicio_serasa.services.db.security import *
from unittest import mock, TestCase


class TestSecurity(TestCase):
    def test_normalize_key_work(self):
        self.assertEqual((5, [7, 4, 4, 1, 2]), normalize_key("arroz"))

    @mock.patch("exercicio_serasa.services.db.security.normalize_key")
    def test_crypt_work(self, mock_normalize_key):
        mock_normalize_key.return_value = (22, [0, 1, 0, 7, 2, 9, 7, 4, 5, 7, 2, 6, 1, 9, 2, 9, 4, 1, 0, 5, 6, 1])
        palavra = [
            " 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,.;/áéíóúÁÉÍÓÚàÀãõÃÕüÜ",
            "mübõaÚfSÀy,NtvKcJ0ouICHB nT2kzóÕD;Lw/3rlZÉRÃ4ãP6éjiÜAGÍYM8OX5àÓWsVqFUxEpÁQ7hgúá1í9.de",
            ".UPeZO/hIxJlzgcáCÀL5õsvE7au1fóÍ,Q8úq9DéãHGXr3jàR ;oyüdíNMÁwiTÜ24tm6nBÕSÓWKÉb0YÃFVAkpÚ",
            "fuNDEbmlJ2RÀãovCUGta8AÓ,áXúFYÕWQwh/ rZ1MeSTOPs3yd.IKÜ5BknÃqóíÉ7Íõc4zgÚ9üVjéxHàÁ;0L6ip",
            "0É;2vtóQwqaIiKzcBVyG9éãCfsHkmüPFngx/8 WÕeíÜÍDÃULu.ZoMhpbú,NAOÚJ5á7r3ÀSlÓ4T6d1RõàÁjEYX",
            "JhYb1OGÁáIKremü78H2Bsgã.õ69P/Qu;AlVWXàzoCf4íDSNZóÜtRkyipÍajÉ ÓqéFMdúLUEn5xTÕ3,0ÃvÚwcÀ",
            "ÜãÃHYaQÁi94rGm8ÀxZcàóy2kÚqvU7FouP3VzLXBlgjúÍáIJApWsKtÓCwfdSéíeM0hnbõü1OÕ,T5 ./N6D;ERÉ",
            "Zõsd8u1V6aGÀÓÚ/9ÁíÃ2áRH5;X4AvCãWwDüióxÉéjcgJKoyú.eIf7YzhTtUSbBO,mP3pqQÜN0ÍàEkrFlnMLÕ ",
            "6;áMua /.ÍcéP2Ysm,ówÁ347í9iJLnpFHK5àeARÜDõúZüÀgQoÓyqkxObÚÉvBlNrXWÕCETIhd8zV10GtSfÃUjã",
            "hÉÍ,P7úN;zQõÁocDUàI6rC qOB0ãítMYa8.3pÃyT/2ükdEKxf5éJZÓÜÀRuiH4sASXFó91áwjLGWvlÚngbVÕem",
        ]
        self.assertEqual(" mübõaÚfSÀy,NtvKcJ0ouICHB nT2kzóÕD;Lw/3rlZÉRÃ4ãP6éjiÜAGÍYM8OX5àÓWsVqFUxEpÁQ7hgúá1í9.de.UPeZ"
                         "O/hIxJlzgcáCÀL5õsvE7au1fóÍ,Q8úq9DéãHGXr3jàR ;oyüdíNMÁwiTÜ24tm6nBÕSÓWKÉb0YÃFVAkpÚfuNDEbmlJ2R"
                         "ÀãovCUGta8AÓ,áXúFYÕWQwh/ rZ1MeSTOPs3yd.IKÜ5BknÃqóíÉ7Íõc4zgÚ9üVjéxHàÁ;0L6ip0É;2vtóQwqaIiKzcB"
                         "VyG9éãCfsHkmüPFngx/8 WÕeíÜÍDÃULu.ZoMhpbú,NAOÚJ5á7r3ÀSlÓ4T6d1RõàÁjEYXJhYb1OGÁáIKremü78H2Bsgã"
                         ".õ69P/Qu;AlVWXàzoCf4íDSNZóÜtRkyipÍajÉ ÓqéFMdúLUEn5xTÕ3,0ÃvÚwcÀÜãÃHYaQÁi94rGm8ÀxZcàóy2kÚqvU7"
                         "FouP3VzLXBlgjúÍáIJApWsKtÓCwfdSéíeM0hnbõü1OÕ,T5 ./N6D;ERÉZõsd8u1V6aGÀÓÚ/9ÁíÃ2áRH5;X4AvCãWwDü"
                         "ióxÉéjcgJKoyú.eIf7YzhTtUSbBO,mP3pqQÜN0ÍàEkrFlnMLÕ 6;áMua /.ÍcéP2Ysm,ówÁ347í9iJLnpFHK5àeARÜD"
                         "õúZüÀgQoÓyqkxObÚÉvBlNrXWÕCETIhd8zV10GtSfÃUjãhÉÍ,P7úN;zQõÁocDUàI6rC qOB0ãítMYa8.3pÃyT/2ükdEK"
                         "xf5éJZÓÜÀRuiH4sASXFó91áwjLGWvlÚngbVÕem", crypt(palavra))

        mock_normalize_key.return_value = (5, [7, 4, 4, 1, 2])
        self.assertEqual("Àmmn9", crypt("arroz"))

    @mock.patch("exercicio_serasa.services.db.security.normalize_key")
    def test_uncrypt_work(self, mock_normalize_key):
        mock_normalize_key.return_value = (5, [7, 4, 4, 1, 2])
        self.assertEqual("arroz", uncrypt("Àmmn9"))
