from flask import Response
import json


def gera_response(status, nome_conteudo, conteudo, mensagem=None):
    body = {nome_conteudo: conteudo}
    if mensagem:
        body["mensagem"] = mensagem

    return Response(json.dumps(body), status=status, mimetype="application/json")