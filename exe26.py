cont = 0
somaidade = 0
mediaidade = 0
maiorh = 0
nomevelho = ''
for c in range(1, 5):
    nome = str(input("digite o nome da {} pessoa: ".format(c))).strip()
    idade = int(input('digite a idade da {} pessoa: '.format(c)))
    sexo = str(input('digite o sexo da {} pessoa (M/F): '.format(c))).strip()
    somaidade += idade
    if sexo in 'fF':
        if idade < 20:
            cont += 1
    if sexo in 'mM' and c == 1:
        maiorh = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maiorh:
        maiorh = idade
        nomevelho = nome
mediaidade = somaidade / 4
print('existem {} mulheres com menos de 20 anos'.format(cont))
print('o homem mais velho tem {} e se chama {}'.format(maiorh, nomevelho))
print('a media das idades é de {} '.format(mediaidade))
