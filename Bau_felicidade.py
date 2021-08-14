try:
    linha1 = input().rstrip().split()
except:...

moedas_pesos = input().rstrip().split()
moedas_pesos= [int(c) for c in moedas_pesos]
total_pesos = sum(moedas_pesos)
diferenca = total_pesos%2
print(diferenca)


