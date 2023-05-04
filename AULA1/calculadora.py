#calculadora

oper = input("Digite qual operção você deseja execultar")
num1 = int(input('Digite um número'))
num2 = int(input('Digite outro número'))

som = " soma"
subtra = " subtração"
divisao = ' divisaõ'
multipli = ' multiplicação'

if oper == som:
     total = num1 + num2
     print(f'O resultado da Soma é{total}')
elif oper == subtra:
    total = num1 - num2
    print(f'O resultado da Subtração é{total}')
elif oper == divisao:
    total = num1 / num2
    print(f'O resultado da Divisão é {total}')
elif oper == multipli:
    total = num1 * num2
    print(f'O Resultado da Multiplicação é {total}')
else:
    print('Você não escolheu nenhuma operação')

