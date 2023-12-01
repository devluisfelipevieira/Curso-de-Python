frase='Curso em Vídeo Python'
print(frase[9:15:3])
print(len(frase))#-> Comprimento da srt, frase
print(frase.count('o',0,13))#-> Contagem da letra 'o' em frase(de 1 a 12)
print(frase.find('deo'))#-> Em qual momento aparece as letras 'deo' em sequência em frase
print('curso' in frase)#-> Analisa se 'curso' está dentro de frase
print(frase.replace('Python','Android'))
#î Muda a variavel frase de 'Curso em Vídeo Python', para 'Curso em Vídeo Android'
print(frase.upper())#-> Muda todas as letras em maiúsculas
print(frase.lower())#-> Muda todas as letras para minúsculas
print(frase.capitalize())#-> A primeira letra da frase terá letra maiúscula
print(frase.title())#-> As primeiras letras das palavras terão letra maiúscula

frase='   Aprenda Python  '
print(frase.strip())#-> remove os espaços do começo e do final
print(frase.rstrip())#-> remove os espaços do lado direito (right)
print(frase.lstrip())#-> remove os espaços do lado esquerdo (left)
#com o find tambem é possivel usar o r(right) e o l(left)

frase='Curso em Vídeo Python'
print(frase.split())#-> além de remover os espaços do começo e do final, tbm divide as palavras
print('-'.join(frase))#-> trasforma a string em uma só, com algo entre as letras
print(frase.lower().find('vídeo'))#-> dois comandos combinados
print(frase.split()[0])#-> mostra o primeiro item da lista (curso)
print(frase.split()[0][2])#-> localiza a letra do item







