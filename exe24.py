tot = 0
ton = 0
for c in range(1, 7+1):
    c = int(input("digite a idade: "))
    if c >= 21:
        tot += 1
    else:
        ton +=1
print("{} pessoas atingiram a maioridade e {} nao atingiram ainda".format(tot,ton),end='')