
''' Ao reler o desafio, percebi que estava sendo solicitado banco de dados relacional porém havia entendido que
estava sendo solicitado DB Não-Relacional (erro de interpretação), assim o código teve que ser reiniciado'''

import pyodbc # Biblioteca do banco de dados SQl

dados_conexao = (
    "Driver={SQL Server};"
    "Server=LAPTOP-B00KFP26;"
    "Database=PubFuture;"
)

conexao = pyodbc.connect(dados_conexao)

cursor = conexao.cursor()

'''def Cad_Rec():                                             # Irá Cadastrar uma nova receita
    rv = float(input('Valor R$: '))
    rdr = input('Data do recebimento: ')
    rd = str(input('Descrição: '))
    rc = str(input('Conta: ').upper())
    rt = str(input('Tipo de Receita: ').upper())
    Receita = {
        'valor': rv,
        'dataRecebimento': rdr,
        'descrição': f'{rd}',
        'conta': f'{rc}',
        'tipoReceita': f'{rt}'
    }
    collection_rec.insert_one(Receita)

    rv = valor
    rdr = dataRecebimento
    rd = descrição
    rc = conta
    rt = tipoReceita (salário, presente, prêmio, outros)


def Cad_Des():                                             # Irá Cadastrar uma nova despesa
    dv = float(input('Valor R$: '))
    ddr = input('Data do recebimento: ')
    dd = str(input('Descrição: '))
    dc = str(input('Conta: ').upper())
    dt = str(input('Tipo de Receita: ').upper())
    Despesa = {
        'valor': dv,
        'dataRecebimento': ddr,
        'descrição': f'{dd}',
        'conta': f'{dc}',
        'tipoDespesa': f'{dt}'
    }
    collection_des.insert_one(Despesa)

    dv = valor
    ddr = data do Recebimento
    dd = descrição
    dc = conta
    dt = tipo da Despesa (salário, presente, prêmio, outros

        rvalor decimal(10, 2),
        rdata date,
        rdescrição varchar(50),
        rconta varchar(50),
        rtipo varchar(50),
        dvalor decimal(10, 2),
        ddata date,
        ddescrição varchar(50),
        dconta varchar(50),
        dtipo varchar(50),
		csaldo decimal(10, 2),
		ctipo varchar(50),
		cintf varchar(50)'''
