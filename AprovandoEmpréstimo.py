casa = int(input("Qual o valor da casa: R$"))
salario = int(input("Qual o seu salário: R$ "))
prestacao = int(input("Em quantos meses voce ira pagar: "))
mensal = casa/prestacao
minimo = salario * 0.3
print("Voce terá que pagar {:.2f} em {} meses".format(mensal,prestacao))
if mensal >= minimo:
    print("Voce nao pode financiar esta casa")
else:
    print("Voce poderá financiar esta casa")
