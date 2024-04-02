cidade = str(input("Digite o nome da sua cidade: ")).upper()
cidades = cidade.split()
if cidades[0] == "SANTO":
    print("A sua cidade começa com Santo")
else:
    print("A sua cidade Não começa com Santo")
print("nome da cidade: {}".format(cidade))