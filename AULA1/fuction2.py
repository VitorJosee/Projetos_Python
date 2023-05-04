x = 1
def escopo():
    def outrafuncao():
        y = 3
        print(x,y)
    outrafuncao()
    print(x)
escopo()

n1 = input('Digite um valor: ')
n2 = input('Digite o segundo valor: ')
if n1.isdigit():
    n1 = int(n1)

if n2.isdigit():
    n2 = int(n2)


def calculadora():
    def soma(a,b):
        rest = a + b
        print(rest)
    def mult(a,b):
        rest2 = a * b
        print(rest2)
    def divi(a,b):
        rest3 = a / b
        print(rest3)
    def sub(a,b):
        rest4 = a - b
        print(rest4)
    sub(n1,n2)
    soma(n1,n2)
    mult(n1,n2)
    divi(n1,n2)
calculadora()
