# Finanças (Emprestimos)
# Nome / Valor (capital) /No de meses(Período) / Taxa de juros (%)
# juros = capital * periodo * taxa
# Montante = Capital + juros
# Saída = Nome + Capital + Montante

def currency(value):
    a = '{:,.2f}'.format(float(value))
    b = a.replace(',','v')
    c = b.replace('.',',')
    return c.replace('v','.')

def calc_juros():
    print('Bom dia! Faça a sua simulação.')
    nome = input('Nome: ')
    capital = float(input('valor: '))
    periodo = int(input('Número de meses: '))
    taxa = float(input('Taxa de juros: '))

    juros = capital * periodo * taxa
    montante = capital + juros
    saida = f"Olá {nome}! Para fazer um empréstimo de R$ {currency(round(capital,2))}, no final irá ter pago R$ {currency(round(montante,2))}"
    print(saida)

calc_juros()