#Calculadora de Média
n1 = input("Digite o 1° valor: ")
n2 = input("Digite o 2° valor: ")
n3 = input("Digite o 3° valor: ")
n1_tratado = n1.replace(',','.')
n2_tratado = n2.replace(',','.')
n3_tratado = n3.replace(',','.')
if n1.isdigit() or n1.isnumeric() or n1.isdecimal() and n2.isdigit() or n2.isnumeric() or n2.isdecimal() and n3.isdigit() or n3.isnumeric() or n3.isdecimal():
    fn1 = float(n1_tratado)
    fn2 = float(n2_tratado)
    fn3 = float(n3_tratado)
    media = (fn1+fn2+fn3)/3
    print("A média é: ",media)
else:
    print("Digite apenas números.")
#fim
