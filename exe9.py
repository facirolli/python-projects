velo = int(input("Qual a velocidade do carro em KM/H: "))
if velo > 80:
    multa = (velo-80)*7
    print("Seu carro excedeu o limite de velocidade e voce foi multado em R${}".format(multa))
else:
    print("Não houve excesso de velocidade")