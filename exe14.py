salario = float(input("digite o salario: "))
if  (salario > 1250.00):
    salario2 = salario + (salario * 0.10)
if (salario < 1250.00):
    salario2 = salario + (salario * 0.15)

print("o salario de {} foi para {}".format(salario, salario2))