peso = float(input('Digite seu peso? (Kg) '))
altura = float(input('Digite sua altura? (m) '))
imc = peso/(altura**2)
print(f'O imc dessa pessoa é {imc:.1f}')
if(imc < 18.5):
    print('Abaixo do peso')
if(imc >= 18.5 and imc < 25): 
    print('Peso ideal')
if(imc >= 25 and imc < 30):
    print('Sobrepeso')
if(imc >=30 and imc < 40):
    print('Obesidade')
if(imc>=40):
    print('Obesidade mórbida')