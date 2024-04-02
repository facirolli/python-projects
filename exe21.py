num = int(input('primeiro termo: '))
razao = int(input("Razao: "))
dec = num + (11 - 1) * razao
for c in range(num, dec, razao):
    print('{}'.format(c), end='-> ')
print("acabou")