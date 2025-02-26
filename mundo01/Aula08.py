import math
import emoji

# pip freeze  -> para saber todas as biblioteca instaladas
# documentação das bibliotecas https://pypi.org/project/emoji/

#print(f'O valor a pagar é R$ {60 * 8.0 + (.15 * 8):.2f}')

num = int(input('Digite um número: '))
raiz =  math.sqrt(num)
print(f'A raiz quadrada de {num} é {raiz:.2f}')

print(emoji.emojize('Python is :thumbs_up:'))
print(emoji.emojize('Python is :thumbsup:', language='alias'))
print(emoji.demojize('Python is 👍'))
print(emoji.emojize("Python is fun :red_heart:"))
print(emoji.is_emoji("👍"))
