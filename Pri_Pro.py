def Soma(a, b):
        aux = int(a) + int(b) #Soma dos valores (int() é necessário pra converter de String para Int)
        return aux
def Subt(a, b):
        aux = int(a) - int(b) #Subtração dos valores
        return aux

Opc = 1 #Varíavel opção do usuário

#Varíaveis a serem somadas/subtraidas/multiplicadas/divididas
x, y = 0, 0
Resu = 0

#Menu
Opc = input("Calculadora: \n1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão\n") #Entrada do usuário

#Opção Soma
if Opc == "1":
        x = input("Por favor informe o primeiro número a ser somado: ") #Coleta do primeiro valor
        y = input("Por favor informe o segundo número a ser somado: ") #Coleta do segundo valor
        resu = Soma(x, y) #Chama a função Soma e executa a operação
elif Opc == "2":
        x = input("Por favor informe o primeiro número a ser subtraido: ") #Coleta do primeiro valor
        y = input("Por favor informe o segundo número a ser subtraido: ") #Coleta do segundo valor
        resu = Subt(x, y) #Chama a função Subt e executa a operação
else:
        print("Erro") #Caso pule o if

print("O resultado é", resu) #Mostra o resultado da operação na tela