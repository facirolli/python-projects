nome = str(input("digite seu nome completo: "))
nomeS = nome.split()
print("o primeiro nome é {}".format(nomeS[0]))
print("o ultimo nome é {}".format(nomeS[len(nomeS)-1]))