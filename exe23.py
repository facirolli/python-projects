frase = str(input('digite uma frase: ')).split()
frasej = ''.join(frase).lower()
if frasej == frasej[::-1]:
    print("é um palidromo")
else:
    print("nao é um palidromo")