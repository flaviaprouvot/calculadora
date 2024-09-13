import os

def soma (a,b):
    return(a+b)
def subtracão (a,b):
    return(a-b)
def multiplicacao (a,b):
    return(a*b)
def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero"

while True:
    a= int(input("Digite o primeiro número:"))
    b=int(input("Digite o segundo número:"))
    op=str(input("Digite a operação + - * /:"))

    if op=="x":
        break

    elif op == "+":
        print (soma(a,b))
    elif op == "-":
        print (subtracão(a,b))
    elif op == "*":
        print (multiplicacao(a,b))
    elif op == "/":
        print (divisao(a,b))

    else:
        print ("Opção inválida")

os.system("pause")
os.system("cls")
