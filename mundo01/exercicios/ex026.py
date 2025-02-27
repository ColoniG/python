print("#" * 140, "\n")
# Começar o código apartir daqui
frase = str(input("Digite uma frase: ")) 
frase = " ".join(frase.upper().split())

print(f"Na frase '{frase.capitalize()}' Aparecem A {frase.count("A")} vezes, a primeira vez apareceu na posição {frase.find("A")} e por último na posição {frase.rfind("A")}") 
# Finalizar até aqui
print("")                                             
print("#" * 140)
