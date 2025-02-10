# isspace() é um método como os outros
algo = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(algo)}')
print(f'Só tem espaço? {algo.isspace()}')
print(f'É um numérico? {algo.isnumeric()}')
print(f'É alfabético? {algo.isalpha()}')
print(f'É alfanumérico? {algo.isalnum()}')
print(f'Está em maiúscula? {algo.isupper()}')
print(f'Está em minúscula? {algo.islower()}')
print(f'Está capitalizada? {algo.istitle()}')


