# Exercise

colombianPesos = int(input("What do you have left in pesos? = $"))
peruvianSoles = int(input("What do you have left in soles? = $"))
brazilianReais = int(input("What do you have left in reais? = $"))

leftOverCo = colombianPesos * 0.00026
leftOverPe = peruvianSoles * 0.27
leftOverBr = brazilianReais * 0.20

leftOverUsd = leftOverCo + leftOverPe + leftOverBr
print(leftOverUsd)
