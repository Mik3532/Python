#nesse programa o usuario vai informar sua idade e o programa vai informar em que grupo ela se encontra 


#usuario vai infromar sua idade 
idade = input("Digite sua idade: ")

#mudando a class da variavel idade para inteiro 
idade = int(idade)


#verificando a condição para ver em que grupo o usuario esta  
if idade < 12:
    print("criançakkkkk")
elif idade < 18:
    print("adolescente")
elif idade < 60:
    print("adulto")
else:
    print("idoso")