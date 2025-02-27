print("#" * 140, "\n")
# Começar o código apartir daqui
numero = int(input("Digite um número de 0 a 9999: "))

print()
print(f"unidade: {numero // 1 % 10}")
print(f"dezena: {numero // 10 % 10}")
print(f"centana: {numero // 100 % 10}")
print(f"milhar: {numero // 1000 % 10}")   
# Finalizar até aqui
print("")
print("#" * 140)
