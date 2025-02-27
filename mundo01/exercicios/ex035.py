print("#" * 140, "\n")
# Começar o código apartir daqui
ab = float(input("Primeiro segmento de reta: "))
cd = float(input("Segundo segmento de reta: "))
ef = float(input("Terceiro segmento de reta: "))


if ab + cd > ef and ab + ef > cd and cd + ef > ab:
    print("O triângulo existe.")
else:
    print("O triângulo não pode existir.")
# Finalizar até aqui
print("")
print("#" * 140)

# \033[0:30:41m
