opc = 1
x, y = 0, 0


print("Calculadora: \n1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão")
opc = input()

if opc == "1":
        x = input("Por favor informe o primeiro número a ser somado: ")
        y = input("Por favor informe o segundo número a ser somado: ")
        soma = int(x)+int(y)
        print("Resultado:", soma)
else:
        print("Erro")