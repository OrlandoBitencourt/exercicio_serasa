from exercicio_serasa.services.users.users import *
from unittest import TestCase, mock
from exercicio_serasa.services.db.security import uncrypt


class Testusers(TestCase):
    def test_create_user_work(self):
        user_dict = dict(name="Fulano de Tal",
                         cpf="012345678912",
                         email="fulano@gmail.com",
                         phone_number="4798852920")

        self.assertTrue(Users().create_user(user_dict))

        self.assertFalse(Users().create_user({}))

    @mock.patch("exercicio_serasa.services.users.users.users", create=True)
    def test_insert_user_work(self, mock_users):
        user_test = Users()

        self.assertFalse(user_test.insert_user())

        user_dict = dict(name="FÕlÀ7BZz7ZMrH",
                         cpf="0b28OúVwIGPH",
                         email="fÕlÀ7B@V.À52soaq",
                         phone_number="4À9axúdabõ")

        user_test.name = user_dict['name']
        user_test.cpf = user_dict['cpf']
        user_test.email = user_dict['email']
        user_test.phone_number = user_dict['phone_number']

        self.assertTrue(user_test.insert_user())

    @mock.patch("exercicio_serasa.services.users.users.users", create=True)
    def test_list_all_users_work(self, mock_users):
        user_test = Users()
        mock_users.find.return_value = True
        self.assertTrue(user_test.list_all_users())

    @mock.patch("exercicio_serasa.services.users.users.users", create=True)
    def test_list_user_work(self, mock_users):
        user_test = Users()
        mock_users.find.return_value = True
        self.assertTrue(user_test.list_user("6092cbc4f9dfc0891202e223"))

    @mock.patch("exercicio_serasa.services.users.users.users", create=True)
    def test_update_user_work(self, mock_users):
        user_test = Users()
        db_user_dict = dict(name="Fulano de Tal",
                            cpf="012345678912",
                            email="fulano@gmail.com",
                            phone_number="4798852920",
                            created_at="",
                            updated_at="")

        generated_user_dict = dict(id="60942601ea239c622b3a6c5d",
                                   name="FÕlÀ7BZz7ZMrH",
                                   cpf="0b28OúVwIGPH",
                                   email="fÕlÀ7B@V.À52soaq",
                                   phone_number="4À9axúdabõ",
                                   created_at="",
                                   updated_at="")

        mock_users.list_user.return_value = db_user_dict
        mock_users.generate_data_users.return_value = generated_user_dict
        mock_users.convert_user_data.return_value = generated_user_dict
        mock_users.new_user_data.return_value = generated_user_dict

        last_user_info = user_test.db.users.find().sort([('$natural', -1)]).limit(1)

        user_data_to_update = dict(id=str(last_user_info[0]['_id']),
                                   name="zcz27IX",
                                   cpf="0b28OúVwIGPH",
                                   email="fÕlÀ7B@V.À52soaq",
                                   phone_number="4À9axúdabõ",
                                   created_at="05-05-20",
                                   updated_at="05-05-20")

        self.assertTrue(user_test.update_user(new_user_data=user_data_to_update, cpf="012345678912"))

    @mock.patch("exercicio_serasa.services.users.users.users", create=True)
    def test_delete_user_work(self, mock_users):
        user_test = Users()

        self.assertFalse(user_test.delete_user("6092cbc4f9dfc0891202e223k"))

        last_user_info = user_test.db.users.find().sort([('$natural', -1)]).limit(1)

        generated_user_dict = dict(id=str(last_user_info[0]['_id']),
                                   name="FÕlÀ7BZz7ZMrH",
                                   cpf=last_user_info[0]['cpf'],
                                   email="fÕlÀ7B@V.À52soaq",
                                   phone_number="4À9axúdabõ",
                                   created_at="",
                                   updated_at="")

        mock_users.generate_data_users.return_value = generated_user_dict

        self.assertTrue(user_test.delete_user(cpf=uncrypt(generated_user_dict['cpf'])))

    def test_convert_user_data_work(self):
        user_test = Users()

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

        self.assertEqual(converted_data, user_test.convert_user_data(original_data))

    def test_generate_data_users_work(self):
        user_test = Users()

        list_data = [{'_id': "6092cbc4f9dfc0891202e223",
                      'name': "Fulano de Tal",
                      'cpf': "00000000000",
                      'email': "fulano@usermail.com",
                      'phone_number': "000",
                      'created_at': "06-05-2021",
                      'updated_at': "06-05-2021 15:02:01"}
                     ]

        converted_data = {'_id': "6092cbc4f9dfc0891202e223",
                          'name': "Fulano de Tal",
                          'cpf': "00000000000",
                          'email': "fulano@usermail.com",
                          'phone_number': "000",
                          'created_at': "06-05-2021",
                          'updated_at': "06-05-2021 15:02:01"
                          }

        self.assertEqual(converted_data, user_test.generate_data_users(list_data))
