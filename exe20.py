soma = 0
for c in range(1,7):
    num = int(input('digite um numero inteiro: '))
    if num % 2 == 0:
        soma += num
        pares = num
print('os numeros são a soma deles é {}'.format(soma))