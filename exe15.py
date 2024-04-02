casa = float(input('digite o valor da casa: '))
salario = float(input('Informe o seu salario: '))
tempo = int(input('Em quantos anos pretende pagar: '))
prest = casa / (tempo * 12)
if(prest >= (salario*0.30)):
    print('O emprestimo sera negado')
else:
    print('O emprestimo sera concedido')