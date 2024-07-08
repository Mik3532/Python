#Criando o HelloWorld

print ("Hello World")


# exemplo de como declarar uma variavel 

nome = "Mik"
sobreNome = "Alves"
curso = "Python"
idade = 23

print (f"Aluno {nome} {sobreNome} de idade {idade} faz o curso de {curso}")
print (type(idade))    #o comando TYPE serve para mostrar o tipo de dado, se ele e inteiro, real ou ate string etc...


# mudando o tipo de variavel de INTEIRO para TEXTO (STRING)
'''idade = str(idade)
print (type(idade))
'''
nome2 = input("Qual seu Nome:")
idade2 = int(input("Digite sua idade: "))
print (f"Ola, Bem vindo(a) '{nome2} voce tem {idade2} anos então voce e corno")
print (type(nome2), type(idade2))





import os
import time

cont = int(input("Digite um numero inteiro: "))

while cont >=0:
    os.system("cls") #limpar o terminal 
    print (f"contagem regressiva: {cont}... ")
    time.sleep(1)#atrasa o proximo comando
    cont -= 1

os.system("cls")
print ("BOOOOMMMMMMM!")
