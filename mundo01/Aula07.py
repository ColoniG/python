# Ordem de Precedência ->  ()  **    *   /   //   %    +   -  (ctrl+shift+L -> ao selecionar uma palavra e apertar os 3 botôes você consegue reescrever todas as palavras iguais)
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print(f'A soma é {n1 + n2}, \no produto é {m} e a', 'divisão é {:.2f}'.format(d), end=' ')
print(f'A divisão inteira é {di} e potência {e}')




print()
print('='*100)
print('DICAS')
nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {:20}!' .format(nome))
print('Prazer em te conhecer {:>20}!' .format(nome))
print('Prazer em te conhecer {:<20}!' .format(nome))
print('Prazer em te conhecer {:^20}!' .format(nome))
print('Prazer em te conhecer {:=^20}!' .format(nome))
