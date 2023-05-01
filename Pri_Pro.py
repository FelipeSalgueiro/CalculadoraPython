def Soma(a, b):
    aux = int(a) + int(b) #Soma dos valores (int() é necessário pra converter de String para Int)
    return aux
def Subt(a, b):
    aux = int(a) - int(b) #Subtração dos valores
    return aux
def Mult(a, b):
    aux = int(a) * int(b) #Multiplicação dos valores
    return aux

Opc = "" #Varíavel opção do usuário

#Reprint do menu para reuso (se desejado)
while(Opc != "5"):
    #Varíaveis a serem somadas/subtraidas/multiplicadas/divididas
    x, y = 0, 0

    #Varíavel responsável por armazenar o resultado
    Resu = 0

    #Menu
    Opc = input("Calculadora: \n1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão\n5 - Sair \n") #Entrada do usuário

    #Opção Soma
    if Opc == "1":
        x = input("Por favor informe o primeiro número a ser somado: ") #Coleta do primeiro valor
        y = input("Por favor informe o segundo número a ser somado: ") #Coleta do segundo valor
        resu = Soma(x, y) #Chama a função Soma e executa a operação

    #Opção Subtração
    elif Opc == "2":
        x = input("Por favor informe o primeiro número a ser subtraido: ") #Coleta do primeiro valor
        y = input("Por favor informe o segundo número a ser subtraido: ") #Coleta do segundo valor
        resu = Subt(x, y) #Chama a função Subt e executa a operação

    #Opção Multiplicação
    elif Opc == "3":
        x = input("Por favor informe o primeiro número a ser multiplicado: ") #Coleta do primeiro valor
        y = input("Por favor informe o segundo número a ser multiplicado: ") #Coleta do segundo valor
        resu = Mult(x, y) #Chama a função Mult e executa a operação

    #Mostrar resultado apenas se escolher executar alguma operação
    if(Opc == "1" or Opc == "2" or Opc == "3" or Opc == "4"):
        print("O resultado é", resu) #Mostra o resultado da operação na tela
        input("Clique no Enter para prosseguir")#Para que o código espere o usuário ver o resultado antes de fechar

    #Caso o usuário coloque uma entrada inválida
    elif(Opc != "5"):
        print("Por favor digite um valor válido (Entre 1 e 5)!") #Verificar entrada do usuário
        input("Clique no Enter para prosseguir")#Para que o código espere o usuário ver o resultado antes de fechar