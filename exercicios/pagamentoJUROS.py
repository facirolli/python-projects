print('{:=^40}'.format('LOJA'))
preco = float(input('Preço das compras: '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista/cheque
[ 2 ] à vista cartão
[ 3 ] 2x cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('qual é a opção? '))
if(opcao == 1):
    tot = preco - (preco * 0.10)
elif(opcao == 2):
    tot = preco - (preco * 0.05)
elif(opcao == 3):
    tot = preco 
    parcela = tot/2
    print("Sua compra será parcelada em 2x de R${:.2f}".format(parcela))
elif(opcao == 4):
    tot = preco + (preco * 0.20)
    totparcelas = int(input('Quantas parcelas?'))
    parcela = tot/totparcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparcelas,parcela))
else:
    tot = preco
    print('OPÇÃO INVÁLIDA')
print("Sua compra de R${:.2f} vai custar R${:.2f} no final.".format(preco,tot))