from flask import Flask, request, Response
import requests
import json
from exercicio_serasa.services.orders.orders import Orders
from exercicio_serasa.services.db.db import Database
from exercicio_serasa.services.db.response import gera_response

app = Flask(__name__)
db = Database()


@app.route("/health-check")
def health_check():
    return "working!"


@app.route("/new-order/<cpf>", methods=['POST'])
def create_order(cpf: str):
    order = Orders()

    user_data = requests.get(f'http://127.0.0.1:5001/user/{cpf}')
    crypted_user_info = user_data.json()
    if crypted_user_info['mensagem'] == 'ok':
        user_info = order.convert_user_data(crypted_user_info['user'])

        raw_request = request.data.decode("utf-8")
        dict_values = json.loads(raw_request)

        dict_values['user_id'] = user_info['id']

        dict_values['total_value'] = order.calculate_total(dict_values['item_quantity'], dict_values['item_price'])

        if order.create_order(dict_values) is True and order.insert_order() is True:
            order_info = [user_info, dict_values]
            return gera_response(200, "order", order_info, "created")

        return gera_response(400, "order", {}, "Error, unable to insert order.")

    return gera_response(400, "order", {}, "Error, unable to find user info.")


@app.route("/orders", methods=['GET'])
def list_all_orders():
    order = Orders()
    orders_list = []

    try:
        order_list = order.list_all_orders()

        for o in order_list:
            o['_id'] = str(o['_id'])
            orders_list.append(o)

        if len(orders_list) > 0:
            return gera_response(200, "orders", orders_list, "ok")
    except Exception as erro:
        print(str(erro))

    return gera_response(400, "orders", {}, "Error, unable to find any order.")


@app.route("/orders/<cpf>", methods=['GET'])
def list_order_by_cpf(cpf: str):
    order = Orders()
    orders_list = []

    user_data = requests.get(f'http://127.0.0.1:5001/user/{cpf}')
    crypted_user_info = user_data.json()

    if crypted_user_info['mensagem'] == 'ok':
        user_info = order.convert_user_data(crypted_user_info['user'])
        try:
            order_list = order.list_order_by_user(user_info['id'])

            for o in order_list:
                o['_id'] = str(o['_id'])
                orders_list.append(o)

            if len(orders_list) > 0:
                order_info = [user_info, orders_list]
                return gera_response(200, "orders", order_info, "ok")
        except Exception as erro:
            print(str(erro))

        return gera_response(400, "orders", {}, "Error, unable to find orders.")

    return gera_response(400, "orders", {}, "Error, unable to find user info.")


@app.route("/delete-order/<id>", methods=['POST'])
def delete_order(id: str):
    order = Orders()

    if order.delete_order(id) is True:
        return gera_response(200, "order", {}, "deleted")

    return gera_response(400, "order", {}, "Error, unable to find and delete order.")


@app.route("/update-order/<id>", methods=['PUT'])
def update_user(id: str):
    order = Orders()

    raw_request = request.data.decode("utf-8")
    dict_values = json.loads(raw_request)

    dict_values['total_value'] = order.calculate_total(dict_values['item_quantity'], dict_values['item_price'])

    if order.update_order(id, dict_values) is True:
        return gera_response(200, "order", dict_values, "updated")

    return gera_response(400, "order", {}, "Error, unable to find and update order.")


if __name__ == "__main__":
    app.run(debug=True, port=5002)
