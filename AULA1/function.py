def imprimir():
    print('texto')
    print('texto2')

imprimir()

def imprimi(a,b,c):
    print('a,b,c')

imprimi(1,2,3)
imprimi(4,4,5)

def saudacao(a):
    print('Olá, Caixa´da água')

saudacao(1)

n1 = input('Digite um valor: ')
n2 = input('Digite o segundo valor: ')

if n1.isdigit():
    n1 = int(n1)

if n2.isdigit():
    n2 = int(n2)

def soma(a,b,c):
    rest = n1 + n2
    print(f'O resultado da soma é: {rest}')

soma(1,2,3)

def mult (a,b,c):
    rest2 = n1 * n2
    print(f'O resultado da multiplicação é: {rest2}')

mult(1,2,3)

def divi (a,b,c):
    rest3 = n1 / n2
    print(f'O resultado da divisão é: {rest3}')

divi(1,2,3)

def subt (a,b,c):
    rest4 = n1 - n2
    print(f'O resultado da subtração é: {rest4}')

subt(1,2,3)

def múltiplo(a, b):
    return a % b == 0

print(f"múltiplo(16,8) == True  -> obtido: {múltiplo(16,8)}")

def múltiplo1(a, b):
    return a % b == 0

print(f"múltiplo(15,3) == True  -> obtido: {múltiplo1(15,3)}")

def múltiplo2(a, b):
    return a % b == 0

print(f"múltiplo(10,2) == True  -> obtido: {múltiplo2(10,2)}")











