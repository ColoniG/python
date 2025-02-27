print("#" * 140, "\n")
# Começar o código apartir daqui
nome = str(input("Digite seu nome completo: "))
nome = nome.split()

print(" ".join(nome).upper())
print(" ".join(nome).lower())
print(f"'{" ".join(nome)}' tem {len("".join(nome))} letras!")   
print(f"'{nome[0]}' tem {len(nome[0])} letras!")
# Finalizar até aqui
print("")
print("#" * 140)
