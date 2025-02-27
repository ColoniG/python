from datetime import date

print("#" * 140, "\n")
# Começar o código apartir daqui
ano = int(input("Digite um ano ou 0 para o ano atual: "))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano de {ano}, é um ano BISSEXTO!")
else:
    print(f"O ano de {ano}, NÃO é um ano BISSEXTO!")
# Finalizar até aqui
print("")
print("#" * 140)
