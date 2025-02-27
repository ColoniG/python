from random import choice

print("#" * 140, "\n")
# Começar o código apartir daqui
n1 = str(input("Primeiro aluno: "))
n2 = str(input("Segundo aluno: "))
n3 = str(input("Terceiro aluno: "))
n4 = str(input("Quarto aluno: "))
lista = [n1, n2, n3, n4]
print(f"O aluno escolhido foi {choice(lista)}!")
# Finalizar até aqui
print("")
print("#" * 140)

