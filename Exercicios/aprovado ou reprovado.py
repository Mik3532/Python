#solicitando dados do usuario 
nome  = (input("Digite o Nome do Aluno:"))
idade = (input("Digite a idade do aluno:"))
cpf = (input("Digite o CPF do Auno:"))

#alterando a class da variavel idade de string para float
idade = float(idade)

#solicitando as notas do aluno
n1 = (input("Digite a nota do Primeiro Bimestre:")) 
n2 = (input("Digite a nota do segundo Bimestre:")) 
n3 = (input("Digite a nota do terceiro Bimestre:")) 
n4 = (input("Digite a nota do quarto Bimestre:")) 

#mudando a variavel de string para float
n1=float(n1)
n2=float(n2)
n3=float(n3)
n4=float(n4)


#variavel apra calcular a media do aluno 
media =  (n1+n2+n3+n4)/4


#se o aluno tirou nota 7 acima aprovado, 5 a 6 recuperação, 4 a baixo reprovado
if media  >= 7:
    print(f"O Aluno {nome} Foi Aprovado!")
elif media >=5:
    print(f"O Aluno {nome} Esta de recuperação!")
else:
    print(f"O {nome} está reprovado")

print(15*"-","BOLETIM FINAL",15*"-")
#se o aluno for maior de 18 anos ele pode retirar o boletim 
if idade >=18:
    print(f"O Aluno {nome} de CPF N°: {cpf} Pode retirar o Boletim!")
    print(f"As notas Do curso de Python foram \n1°B: {n1}\n2°B: {n2}\n3°B: {n3}\n4°B: {n4}\nEntão a media foi {media}!")
else:
    print(f"Para retirar o Boletim o Aluno {nome} de CPF N°: {cpf}\nDeve está acompanhado pelo responsavel legal")


print(35*"-")