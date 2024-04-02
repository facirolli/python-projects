def numero_par(numero):
    if numero %2 == 0:
        return "par"
    else:
        return "impar"
num = int(input("digite um numero inteiro para saber se é par ou impar: "))
resultado = numero_par(num)
print("o numero digitado '{}' é um numero {}".format(num,resultado))