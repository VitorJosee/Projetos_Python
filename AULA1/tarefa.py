#Soma
num1 = 28
num2 = 30
total = num1+num2

print('A soma de dois números é:', total)

#Média

nota1 = 10
nota2 = 7
nota3 = 9
nota4 = 10
media= (nota1+nota2+nota3+nota4)/4

print(f'A média desse aluno é:{media}')

#Idade da Pessoa

datanasc = 2003
dataatual = 2022
idade = dataatual-datanasc
print(f'A idade é:{idade}')

#Massa corpora da pessoa

peso = float(input('Digite seu peso'))
altura = float(input('Digite a sua altura'))
imc = peso/(altura*altura)
if imc > 25:
    print('Sobrepeso')
if imc < 24:
    print('Ideal')

print(f'O imc dessa pessoa é:{imc}')

