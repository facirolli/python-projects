a = int(input("digite um numero: "))
b = int(input("digite outro numero: "))
c = int(input("digite mais um numero: "))
maior = a
if b > a and b > c:
        maior = b
if c > a and c > b:
        maior = c
menor = a
if b < a and b < c:
        menor = b
if c < a and c < b :
        menor = c 
print("os numeros são {} {} {} e o maior é {} e o menor {}".format(a, b, c, maior, menor))
    