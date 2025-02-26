import math

print("#" * 140, "\n")
# Começar o código apartir daqui
angulo = float(input("Digite o angulo que você deseja: "))
seno = math.sin(math.radians(angulo))
print(f"O ângulo de {angulo} tem o SENO de {seno:.2f}")
cosseno = math.cos(math.radians(angulo))
print(f"O ângulo de {angulo} tem o COSSENO de {cosseno:.2f}")
tangente = math.tan(math.radians(angulo))
print(f"O ângulo de {angulo} tem a TANGENTE de {tangente:.2f}")
# Finalizar até aqui
print("")
print("#" * 140)
