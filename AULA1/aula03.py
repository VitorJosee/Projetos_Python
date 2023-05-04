r1 = input('Digite a hora que agora: ')
if r1.isdigit():
    r1 = int(r1)

if r1 <= 11:
    print(f'A hora é {r1} Bom Dia')
elif r1 <= 18:
    print(f'A hora é {r1} Boa Tarde ')
else:
    print(f'A hora é {r1} Boa Noite')



