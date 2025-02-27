print("#" * 140, "\n")
# Começar o código apartir daqui
sal = float(input("Digite seu salário: \n"))
if sal > 1250:
    aum = sal + (sal * 10 / 100)
    print("Com o aumento de 10%, o seu salário foi de R${:.2f} para R${:.2f}.".format(sal, aum))
else:
    aum = sal + (sal * 15 / 100)
    print("Com o aumento de 15%, o seu salário foi de R${:.2f} para R${:.2f}.".format(sal, aum))
# Finalizar até aqui
print("")
print("#" * 140)
