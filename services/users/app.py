from flask import Flask, request
import json
from users import Users
from db.db import Database
from db.response import gera_response

app = Flask(__name__)
db = Database()


@app.route("/health-check")
def health_check():
    return "working!"


@app.route("/user", methods=['POST'])
def create_user():
    user = Users()

    raw_request = request.data.decode("utf-8")
    dict_values = json.loads(raw_request)

    if user.create_user(dict_values) is True and user.insert_user() is True:
        return gera_response(200, "user", dict_values, "created")

    return gera_response(400, "user", {}, "Error, unable to insert user.")


@app.route("/user/<cpf>", methods=['GET'])
def list_user_by_cpf(cpf: str):
    user = Users()

    try:
        user_list = user.list_user(cpf)
        user_dict = user.generate_data_users(user_list)
        if user_dict is not None:
            return gera_response(200, "user", user_dict, "ok")
    except Exception as erro:
        print(str(erro))

    return gera_response(400, "user", {}, "Error, unable to find user.")


@app.route("/users", methods=['GET'])
def list_all_users():
    user = Users()
    users_list = []

    try:
        user_list = user.list_all_users()

        for u in user_list:
            u['_id'] = str(u['_id'])
            users_list.append(u)

        if len(users_list) > 0:
            return gera_response(200, "users", users_list, "ok")
    except Exception as erro:
        print(str(erro))

    return gera_response(400, "users", {}, "Error, unable to find any user.")


@app.route("/delete-user/<cpf>", methods=['POST'])
def delete_user(cpf: str):
    user = Users()

    if user.delete_user(cpf) is True:
        return gera_response(200, "user", {}, "deleted")

    return gera_response(400, "user", {}, "Error, unable to find and delete user.")


@app.route("/update-user/<cpf>", methods=['PUT'])
def update_user(cpf: str):
    user = Users()

    raw_request = request.data.decode("utf-8")
    dict_values = json.loads(raw_request)

    if user.update_user(cpf, dict_values) is True:
        return gera_response(200, "user", dict_values, "updated")

    return gera_response(400, "user", {}, "Error, unable to find and update user.")


# if __name__ == "__main__":
#     app.run(debug=True)
# , port=5001)
