import os
os.system("cls")
while True:
    
    pergunta = input("Deseja assistir um filme? sim/nao :") .lower()

    if pergunta == "sim":

        print (15*'-',"CineCapy",15*'-')
        print ("SALA 1:  CLASSIFICAÇÃO: LIVRE- Capivara Astronalta")
        print ("SALA 2:  CLASSIFICAÇÃO: LIVRE- Terror da Capivara") 
        print ("SALA 3:  CLASSIFICAÇÃO: LIVRE- Ta Chuvendo Capivara")
        print ("SALA 4:  CLASSIFICAÇÃO: +18- 50Tons de Capivara")
        print ("SALA 5:  CLASSIFICAÇÃO: +18- American Capivara")

        filme = input("Digite a Sala para ver o filme de sua escolha 1,2,3,4,5:")
        idade = input("Digite sua idade por gentileza: ")
        idade = int(idade)

        if filme == "1" :
            print ("Entrada autorizada, Tenha um Otimo filme")
            break
        elif filme == "2":
            print ("Entrada autorizada, Tenha um Otimo filme")
            break
        elif filme == "3":
            print ("Entrada autorizada, Tenha um Otimo filme")
            break
        elif filme == "4" and idade >=18:
            print ("Efetuar o pagamento no guiche Obrigado")
            break
        elif filme == "4" and idade >=18:
            print ("Efetuar o pagamento no guiche Obrigado")
            break
        else:
            print("Idade invalida para assistir esse filme, porfavor selecione um Filme com idade propiada para sua idade :D")

    elif pergunta == "nao":
        print("Certo Obrigado")
        break
    else:
        print("Opção invalida")