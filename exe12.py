def ano_bissexto(ano):
    if ano % 4 == 0:
        return "O ano {} é bissexto".format(ano)
    else:
        return "O ano {} não é bissexto".format(ano)
ano = int(input("digite o ano para saber se é bissexto: "))
saida = ano_bissexto(ano)
print(ano_bissexto(ano))