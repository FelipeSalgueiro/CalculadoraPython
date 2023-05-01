from os import system #Chamando a biblioteca system pra eu poder limpar a tela

#Funções:
#Função de Soma
def Soma(a, b):
    try: #Tenta fazer a soma
        aux = int(a) + int(b) #Soma dos valores (int() é necessário pra converter de String para Int)
    except ValueError: #Caso a ou b tenham valores inválidos
        aux = "NoInt"
    return aux

#Função de Subtração
def Subt(a, b):
    try: #Tenta fazer a subtração
        aux = int(a) - int(b) #Subtração dos valores
    except ValueError: #Caso a ou b tenham valores inválidos
        aux = "NoInt"
    return aux

#Função de Multiplicação
def Mult(a, b):
    try: #Tenta fazer a multiplicação
        aux = int(a) * int(b) #Multiplicação dos valores
    except ValueError: #Caso a ou b tenham valores inválidos
        aux = "NoInt"
    return aux

#Função de Divisão
def Divi(a, b):
    try: #Tenta fazer a divisão
        aux = int(a) / int(b) #Divisão dos valores
    except ValueError: #Caso a ou b tenham valores inválidos
        aux = "NoInt"
    return aux
#Fim Funções


Opc = "" #Varíavel opção do usuário


#Reprint do menu para reuso (se desejado)
while(Opc != "5"):

    #Varíaveis a serem somadas/subtraidas/multiplicadas/divididas
    x, y = 0, 0
    #Varíavel responsável por armazenar o resultado
    Resu = 0


    #Menu
    Opc = input("Calculadora: \n1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão\n5 - Sair \n") #Entrada do usuário


    #Operações:
    #Opção Soma +
    if Opc == "1":
        x = input("\nPor favor informe o primeiro número a ser somado: \n") #Coleta do primeiro valor
        y = input("\nPor favor informe o segundo número a ser somado: \n") #Coleta do segundo valor
        Resu = Soma(x, y) #Chama a função Soma e executa a operação

    #Opção Subtração -
    elif Opc == "2":
        x = input("\nPor favor informe o primeiro número a ser subtraido: \n") #Coleta do primeiro valor
        y = input("\nPor favor informe o segundo número a ser subtraido: \n") #Coleta do segundo valor
        Resu = Subt(x, y) #Chama a função Subt e executa a operação

    #Opção Multiplicação *
    elif Opc == "3":
        x = input("\nPor favor informe o primeiro número a ser multiplicado: \n") #Coleta do primeiro valor
        y = input("\nPor favor informe o segundo número a ser multiplicado: \n") #Coleta do segundo valor
        Resu = Mult(x, y) #Chama a função Mult e executa a operação

    #Opção Divisão /
    elif Opc == "4":
        x = input("\nPor favor informe o dividendo: \n") #Coleta do dividendo
        y = input("\nPor favor informe o divisor: \n") #Coleta do divisor
        Resu = Divi(x, y) #Chama a função Divi e executa a operação
    #Fim das operações


    #Retornos e tratamentos de erro:
    #Mostrar resultado apenas se escolher executar alguma operação
    if((Opc == "1" or Opc == "2" or Opc == "3" or Opc == "4") and Resu != "NoInt"):
        print("\nO resultado é", Resu) #Mostra o resultado da operação na tela
        input("Clique no Enter para prosseguir") #Para que o código espere o usuário

    #Caso o usuário coloque uma entrada inválida
    elif(Opc != "5" and Resu != "NoInt"):
        print("\nPor favor digite um valor válido (Entre 1 e 5)!") #Informar a entrada inválida
        input("Clique no Enter para prosseguir") #Para que o código espere o usuário

    #Caso o usuário digite um valor não inteiro
    elif(Resu == "NoInt"):
        print("\nValor inválido! Por favor digite apenas números!") #Informar a entrada inválida
        input("Clique no Enter para prosseguir") #Para que o código espere o usuário

    #Mensagem de despedida ao usuário
    else:
        print("\nObrigado por usar minha calculadora!")
        input()
    #Fim Retornos e tratamentos de erro

    
    system("cls") #Limpa a tela do terminal