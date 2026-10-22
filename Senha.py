import requests, hashlib

senha = input("Digite sua senha: ")



h = hashlib.sha1(senha.encode())
h = h.hexdigest().upper()
r = requests.get(
    "https://api.pwnedpasswords.com"f"/range/{h[:5]}"
)

vezes = 0 

for linha in r.text.split():
    fim, qtd = linha.split(":")

    if fim == h[5:]:
        vezes = int(qtd)


print(f"Sua senha foi encontrada em vazamentos cerca de {vezes} vezes.")