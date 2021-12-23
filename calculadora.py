#Calculadora
print("Sejam bem vindos a Calculadora")
print("Escolha uma das opções abaixo")
n1 = (input("Digite o 1° valor: "))
n2 = (input("Digite o 2° valor: "))
n1_tratado = float(n1.replace(",","."))
n2_tratado = float(n2.replace(",","."))
if n1.isdigit() or n1.isdecimal() or n1.isnumeric() and n2.isdigit() or n2.isdecimal() or n2.isnumeric():

    print("0 - Sair")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Divisão")
    print("4 - Multiplicação")
    print("5 - Exponênciação")
    operação = int(input("Digite o valor da operação: "))
    if operação == 1:
        soma = n1_tratado+n2_tratado
        print("A soma dos valores é: ",soma)
    elif operação == 2:
        subtração = n1_tratado - n2_tratado
        print("A subtração dos valores é: ",subtração)
    elif operação == 3:
        divisão = n1_tratado / n2_tratado
        print("A divisão dos valores é: ", divisão)
            
else:
    print("Digite apenas números!")    


