#Varíavel opção usuário
opc = 1

#Varíaveis a serem somadas/subtraidas/multiplicadas/divididas
x, y = 0, 0

#Menu
opc = input("Calculadora: \n1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão\n") #Entrada do usuário

#Opção Soma
if opc == "1":
        x = input("Por favor informe o primeiro número a ser somado: ") #Coleta do primeiro valor
        y = input("Por favor informe o segundo número a ser somado: ") #Coleta do segundo valor
        soma = int(x)+int(y) #Soma dos valores (Int() é necessário pra converter de String para Int)
        print("Resultado:", soma) #Mostrar resultado final da soma
else:
        print("Erro") #Caso pule o if