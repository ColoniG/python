print("#" * 140, "\n")
# Começar o código apartir daqui
cidade = str(input("Digite o nome de uma cidade: ")).upper().split()

print(f"A cidade '{" ".join(cidade).title()}' começa com SANTO? {"SANTO" in cidade[0]}") 
# Finalizar até aqui
print("")
print("#" * 140)

"""
cidade = str(input("Digite a cidade: ")).strip()
print(cidade[:5].upper() == "SANTO")  
"""