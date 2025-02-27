from random import randint
from colorama import init, Fore, Back

init()

print("#" * 140, "\n")
# Começar o código apartir daqui
sorteado = randint(0, 5)
numero = int(input("O computador pensou em um número de 0 a 5, tente adivinhar: "))

if numero == sorteado:
    print(Back.WHITE + Fore.GREEN + "Parabéns você acertou")
else:
    print(Back.WHITE + Fore.RED + f"Não foi dessa vez, o número é o {sorteado}!")
# Finalizar até aqui
print(Back.BLACK + "")
print(Fore.WHITE + "#" * 140)
