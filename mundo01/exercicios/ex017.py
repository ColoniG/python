from math import hypot
print("#" * 140, "\n")

c_opo = float(input("Comprimento do cateto oposto: "))
c_adj = float(input("Comprimento do cateto adjacente: "))
hip = (c_opo ** 2 + c_adj ** 2) ** (1/2)
print(f"A hipotenusa vai medir {hip:.2f}.")

# Usando a biblioteca
print(f"A hipotenusa vai medir {hypot(c_opo, c_adj):.2f}.")

print("")
print("","#" * 140)