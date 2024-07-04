#usuario vai digitar os dados
pesoUsuario = float(input("Digite seu peso:"))
carga = float(input("Digite o peso da carga "))

#se o peso total do usuario for menor que 200 ele pode entra se nao vaza
if pesoUsuario + carga <=200:
    print("ta liberado")
else:
    print("vaza mlk")