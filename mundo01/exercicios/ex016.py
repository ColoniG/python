'''
import math

num = float(input("Digite um número: "))
print(f"O número digitado foi {num} e sua parte inteira é {math.trunc(num)}")
'''
from math import trunc

num = float(input("Digite um número: "))
print(f"O número digitado foi {num} e sua parte inteira é {trunc(num)}")

print(f"Parte inteira de outras formas {num:.0f}")
print(f"Parte inteira de outras formas {int(num)}")
