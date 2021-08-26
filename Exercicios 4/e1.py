class Contrato:
    def __init__(self, banco, valor, data):
        self.banco = banco
        self.valor = valor 
        self.data = data

        resultado = f'''
        Banco: {self.banco}
        Valor: {self.valor}
        Data do registro: {self.data}
        '''

        print(resultado)

banco = input('Digite aqui número do banco: ')
valor = input('Digite o valor a ser pago: ')
data = input('Insira a data do registro(dd/mm/aaaa): ')

if(banco == '7'):
    banco = '7 - Itaú'
elif(banco == '1'):
    banco = '1 - Banco do Brasil'
elif(banco == '2'):
    banco = '2 - Caixa'
elif(banco == '3'):
    banco = '3 - Bradesco'
else:
    try:
        raise Exception
    except Exception:
        print('Não temos esse número bancário em nosso banco de dados.')

Contrato(banco, valor, data)