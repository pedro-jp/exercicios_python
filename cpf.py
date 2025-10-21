CPF = str(input("Insira seu CPF:"))

if len(str(CPF)) != 11:
    print( "CPF inválido")
else:
    n1 = int(CPF[0])
    n2 = int(CPF[1])
    n3 = int(CPF[2])
    n4 = int(CPF[3])
    n5 = int(CPF[4])
    n6 = int(CPF[5])
    n7 = int(CPF[6])
    n8 = int(CPF[7])
    n9 = int(CPF[8])
    n10 = int(CPF[9])
    n11 = int(CPF[10])

    soma  = n1 * 10 + n2 * 9 + n3 * 8 + n4 * 7 + n5 * 6 + n6 * 5 + n7 * 4 + n8 * 3 + n9 * 2
    dig1  = soma * 10 % 11 
    if dig1 == n10:
        soma2  = n1 * 11 + n2 * 10 + n3 * 9 + n4 * 8 + n5 * 7 + n6 * 6 + n7 * 5 + n8 * 4 + n9 * 3 + n10 * 2
        dig2 = soma2 * 10 % 11

        if dig2 == n11:
            print("CPF válido")
        else:
            print("CPF inválido")
    else:
        print("CPF inválido")

