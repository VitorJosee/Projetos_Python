Nome = input("Digite seu nome")
print(f'O seu nome é {Nome} e o tipo de variável é'f'{type(Nome)}')

num1 = int(input('Digite um número.'))
num2 = int(input('Digite o outro número'))
total_soma = (num1 + num2)
print(f'O resultado da soma vai ser {total_soma} e o tipo do campo é'f'{type(total_soma)}')

if total_soma > 10:
    print('Verdadeiro')
else:
    print('Falso')

#Tarefa

nome = input("Digite seu nome")
idade = int(input("Digite a Idade."))
ano = int(input("Digite o seu ano de Nascimento"))
peso = float(input('Digite seu peso'))
altura = float(input('Digite a sua altura'))
imc = peso/(altura*altura)

if idade >= 18:
    print('Você é maior de Idade, você pode ser Preso')
else:
    print('Você é menor de Idade, não saiu das fraudas')


print(f'O seu nome é {nome} a sua idade é {idade} o ano que você nasceu {ano} e o seu IMC é {imc}')

if imc <= 18.5:
    print('Abaixo do peso normal')
elif imc <= 24.9:
    print('Peso Normal')
elif imc <= 29.9:
    print('Excesso de peso')
elif imc <= 34.9:
    print('Obesidade classe I')
elif imc <= 39.9:
    print('Obesidade classe II')
else:
    print('Obesidade classe III')

