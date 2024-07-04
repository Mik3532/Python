#O usuario vai digitar um numero e o programa vai verificar se o numero e par ou impa 
n = int(input("digite um numero:"))

#condição se o o resto da divisão dividido por 2 igual a 0, se sim vai ser if se nao vai ser else 
if n % 2 == 0:
    print(f"O Numero que voce digitou: {n} ele e Par ")
else:
    print(f"O numero que voce digitou: {n} ele e Impa  ")