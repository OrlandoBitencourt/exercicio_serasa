# security.py
# -*- coding: iso-8859-1 -*-
#
# Exemplo de um algoritmo de criptografia com chave
# usando o algoritmo criptogr�fico de Cesar

CHAVE = "dona maria tem credito"
MAINTABLE = [
    " 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,.;/������������������",
    "m�b�a�fS�y,NtvKcJ0ouICHB nT2kz��D;Lw/3rlZ�R�4�P6�ji�AG�YM8OX5��WsVqFUxEp�Q7hg��1�9.de",
    ".UPeZO/hIxJlzgc�C�L5�svE7au1f��,Q8�q9D��HGXr3j�R ;oy�d�NM�wiT�24tm6nB�S�WK�b0Y�FVAkp�",
    "fuNDEbmlJ2R��ovCUGta8A�,�X�FY�WQwh/ rZ1MeSTOPs3yd.IK�5Bkn�q���7��c4zg�9�Vj�xH��;0L6ip",
    "0�;2vt�QwqaIiKzcBVyG9��CfsHkm�PFngx/8 W�e���D�ULu.ZoMhpb�,NAO�J5�7r3�Sl�4T6d1R���jEYX",
    "JhYb1OG��IKrem�78H2Bsg�.�69P/Qu;AlVWX�zoCf4�DSNZ��tRkyip�aj� �q�FMd�LUEn5xT�3,0�v�wc�",
    "���HYaQ�i94rGm8�xZc��y2k�qvU7FouP3VzLXBlgj���IJApWsKt�CwfdS��eM0hnb��1O�,T5 ./N6D;ER�",
    "Z�sd8u1V6aG���/9���2�RH5;X4AvC�WwD�i�x��jcgJKoy�.eIf7YzhTtUSbBO,mP3pqQ�N0��EkrFlnML� ",
    "6;�Mua /.�c�P2Ysm,�w�347�9iJLnpFHK5�eAR�D��Z��gQo�yqkxOb��vBlNrXW�CETIhd8zV10GtSf�Uj�",
    "h��,P7�N;zQ��ocDU�I6rC qOB0��tMYa8.3p�yT/2�kdEKxf5�JZ���RuiH4sASXF�91�wjLGWvl�ngbV�em",
]


def normalize_key(key):
    key = [ord(k) % 10 for k in key]
    return len(key), key


def crypt(text):
    key = CHAVE
    table = MAINTABLE
    size, key = normalize_key(key)
    text = list(text)

    pos = 0
    for char in text:
        subtable = table[key[pos % size]]
        new_char_position = table[0].find(char)

        if new_char_position < 0:
            new_char = char
        else:
            new_char = subtable[new_char_position]
        text[pos] = new_char
        pos += 1
    return ''.join(text)


def uncrypt(text):
    key = CHAVE
    table = MAINTABLE
    size, key = normalize_key(key)
    text = list(text)

    pos = 0
    for char in text:
        subtable = table[key[pos % size]]
        new_char_position = subtable.find(char)
        if new_char_position < 0:
            new_char = char
        else:
            new_char = table[0][new_char_position]
        text[pos] = new_char
        pos += 1

    return ''.join(text)


def generate_maintable():
    import random
    print("maintable = [")
    x = list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,.;/������������������")
    for i in range(10):
        print('    "%s",' % (''.join(x)))
        random.shuffle(x)
    print("]")

#import criptografia

# mensagem = "47988888888"
# mensagem_cifrada = crypt(mensagem)
# print("Mensagem original: %s" % (mensagem))
# print("Mensagem cifrada: %s" % (mensagem_cifrada))
# print("Mensagem de retorno: %s" % (uncrypt(mensagem_cifrada)))

# print(uncrypt("0�0�U���h�P"))