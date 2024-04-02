def preço_passagem(distancia):
    if distancia <= 200:
        preço = distancia*0.5
        return preço
    if distancia > 200:
        preço = distancia *0.45
        return preço
dista = float(input("Qual será a distância da viagem?: "))
resultado = preço_passagem(dista)
print("Para a distância de {} KM/H será cobrado o preço de R${}".format(dista,resultado))

