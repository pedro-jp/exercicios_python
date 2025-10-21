salario = float(input("Insira o salário: "))
codigoCargo = str(input("Insira o código do cargo: "))
newSalary = 0
aumento = 0

if salario < 1:
    print("Salário inválido")

else:
    if codigoCargo == 'GER': 
        aumento = salario * 0.1
        newSalary = salario + aumento
    elif codigoCargo == 'ENG': 
        aumento = salario * 0.2
        newSalary = salario + aumento        
    elif codigoCargo == 'TEC': 
        aumento = salario * 0.3
        newSalary = salario + aumento
    else:
        aumento = salario * 0.4
        newSalary = salario + aumento
print("Salário",round(salario,2))
print("Aumento",round(aumento,2))
print("Novo salário",newSalary)