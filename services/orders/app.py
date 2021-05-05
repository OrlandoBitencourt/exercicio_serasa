from flask import Flask, request, Response
import json
from exercicio_serasa.services.users.orders import Orders
from exercicio_serasa.services.db.db import Database
from exercicio_serasa.services.db.response import gera_response