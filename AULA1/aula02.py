nome = input('Digite o seu nome: ')
media_portugeus = float(input('Digite a média de Portugues: '))
media_matematica = float(input('Digite a média de Matemática: '))
media_historia = float(input('Digite a média de História: '))
media_geograifa = float(input('Digite a média de Geografia: '))
media_sociologia = float(input('Digite a média de Sociologia: '))

def media():
   media = (media_portugeus + media_matematica + media_historia + media_geograifa + media_geograifa)/5
   if media >= 7:
       return 'Aprovado'
   return 'Reprovado'
print(media())