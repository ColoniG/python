print("#" * 140, "\n")
# Começar o código apartir daqui
numero = str(input("Digite três números: ")).split()
numero[0] = int(numero[0])
numero[1] = int(numero[1])
numero[2] = int(numero[2])

menor = numero[0]
if numero[1] < numero[0] and numero[1] < numero[2]:
    menor = numero[1]
if numero[2] < numero[0] and numero[2] < numero[1]:
    menor = numero[2]

maior = numero[0]
if numero[1] > numero[0] and numero[1] > numero[2]:
    maior = numero[1]
if numero[2] > numero[0] and numero[2] > numero[1]:
    maior = numero[2]

print(menor, maior, maior + menor)

# Finalizar até aqui
print("")
print("#" * 140)
