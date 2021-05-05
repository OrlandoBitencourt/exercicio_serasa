# security.py
# -*- coding: iso-8859-1 -*-
#
# Exemplo de um algoritmo de criptografia com chave
# usando o algoritmo criptográfico de Cesar

CHAVE = "dona maria tem credito"
MAINTABLE = [
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
    x = list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,.;/áéíóúÁÉÍÓÚàÀãõÃÕüÜ")
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

# print(uncrypt("0ü0õUÉõÉhõP"))