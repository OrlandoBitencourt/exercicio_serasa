def esconde(msg):
    s = ''
    for c in msg: s += chr(ord(c) + 30000)
    return s


def mostra(msg):
    s = ''
    for c in msg: s += chr(ord(c) - 30000)
    return s

msg = "abc"
criptografado = esconde(msg)
print(criptografado)
decriptografado = mostra(criptografado)
print(decriptografado)