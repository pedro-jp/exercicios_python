opcao = 10
eymael = 0
levy = 0
cabo = 0
nulo = 0
branco = 0
totalDeVotos = 0

while opcao != 0:
    opcao = int(input("Insira o voto"))
    if opcao == 1:
        eymael = eymael + 1
        totalDeVotos = totalDeVotos + 1
        print(
            f"Eymael: {eymael / totalDeVotos * 100}% | Levy: {levy / totalDeVotos * 100} | Cabo: {cabo / totalDeVotos * 100} | Nulo: {nulo / totalDeVotos * 100} | Branco: {branco / totalDeVotos * 100}")
    elif opcao == 2:
        levy = levy + 1
        totalDeVotos = totalDeVotos + 1
        print(f"Eymael: {eymael / totalDeVotos * 100}% | Levy: {levy / totalDeVotos * 100} | Cabo: {cabo / totalDeVotos * 100} | Nulo: {nulo / totalDeVotos * 100} | Branco: {branco / totalDeVotos * 100}")
    elif opcao == 3:
        cabo = cabo + 1
        totalDeVotos = totalDeVotos + 1
        print(
            f"Eymael: {eymael / totalDeVotos * 100}% | Levy: {levy / totalDeVotos * 100} | Cabo: {cabo / totalDeVotos * 100} | Nulo: {nulo / totalDeVotos * 100} | Branco: {branco / totalDeVotos * 100}")
    elif opcao == 4 :
        nulo =  nulo +1
        totalDeVotos = totalDeVotos + 1
        print(
            f"Eymael: {eymael / totalDeVotos * 100}% | Levy: {levy / totalDeVotos * 100} | Cabo: {cabo / totalDeVotos * 100} | Nulo: {nulo / totalDeVotos * 100} | Branco: {branco / totalDeVotos * 100}")
    elif opcao == 5:
        branco = branco + 1
        totalDeVotos = totalDeVotos + 1
        print(
            f"Eymael: {(eymael / totalDeVotos) * 100}% | Levy: {levy / totalDeVotos * 100} | Cabo: {cabo / totalDeVotos * 100} | Nulo: {nulo / totalDeVotos * 100} | Branco: {branco / totalDeVotos * 100}")
if eymael > levy and eymael > cabo and eymael > nulo and eymael > branco:
     print ('O CADIDADO EYMAEL FOI O GANHADOR')

if levy > eymael and levy > cabo and levy > nulo and levy > branco:
    print('O CADIDADO Levy FOI O GANHADOR')

if cabo > eymael and cabo > levy and cabo > nulo and cabo > branco:
    print('O CADIDADO Cabo FOI O GANHADOR')

if nulo > eymael and nulo > levy and nulo > cabo and nulo > branco:
    print('A eleição teve mais nulos.')

if branco > eymael and branco > levy and branco > cabo and nulo < branco:
    print('A eleição teve mais branco.')
