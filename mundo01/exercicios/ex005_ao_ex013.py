n = int(input('Digite um número: '))

print(f'### DESAFIO 5 ### Antecessor {n-1} / número digitado "{n}" / {n+1} sucessor!')

print(f'### DESAFIO 6 ### Dobro: {n*2} / Tríplo: {n*3} / Raiz quadrada: {n**0.5}!')

n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))
print(f'### DESAFIO 7 ### A média entre a nota {n1} e a nota {n2} é {(n1+n2)/2}.')

m = float(input('Digite os metros: '))
print('### DESAFIO 8 ### {:.1f} metros, equivalem a {:.1f} centímetros e {:.1f} milímetros.'.format(m, m*100, m*1000))

print(f'### DESAFIO 9 ### Segue abaixo a tabuada de {n}:\n{n} x 1 = {n}\n{n} x 2 = {n*2}\n{n} x 3 = {n*3}\n{n} x 4 = {n*4}\n{n} x 5 = {n*5}\n{n} x 6 = {n*6}\n{n} x 7 = {n*7}\n{n} x 8 = {n*8}\n{n} x 9 = {n*9}\n{n} x 10 = {n*10}\n')

r = float(input('Digite a quantidade de Reais (R$): '))
print('### DESAFIO 10 ### R$ {:.2f} equivalem a {:.2f} dólares na cotação de 3,27.'.format(r, r/3.27))

l1 = float(input('Digite a largura da parede: '))
l2 = float(input('Digite a altura da parede: '))
print('### DESAFIO 11 ### Para pintar a área de {:.2f}m² você precisa de {} litros de tinta.'.format(l1*l2, l1*l2/2))

p = float(input('Digite o preço: '))
print('### DESAFIO 12 ### Com o desconto de {:.2f} (5%) o novo valor é {:.2f}.'.format(p*0.05, p*0.05-p))

p = float(input('Digite o salário: '))
print('### DESAFIO 13 ### Seu salário aumentará {:.2f} (15%), seu novo salário reajustado será: {:.2f}.'.format(p*0.15, p*0.15+p))

print('\n','-'*140,'\n')