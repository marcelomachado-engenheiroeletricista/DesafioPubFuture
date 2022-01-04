########## Importanto bibliotecas ##########

import pyodbc               # Biblioteca OBBC para conetar ao banco de dados SQl
import pandas as pd         # Biblioteca Pandas p/ ler o banco de dados

############################################

########## Fazer conexão com o DB ##########

dados_conexao = (
    "Driver={SQL Server};"
    "Server=LAPTOP-B00KFP26;"
    "Database=PubFuture;"
)

conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

############################################

################ Funções ###################

def Cad_Rec():                                             # Irá Cadastrar uma nova receita
    print('Digite a Receita')
    rv = float(input('Valor R$: '))
    rdr = input('Data do recebimento: ')
    rd = str(input('Descrição: ').upper())
    rc = str(input('Conta: ').upper())
    rt = str(input('Tipo de Receita: ').upper())

    comando = f"""INSERT INTO RECEITAS(rvalor, rdata, rdescrição, rconta, rtipo)
    VALUES
        ({rv}, '{rdr}', '{rd}', '{rc}', '{rt}')"""
    cursor.execute(comando)
    cursor.commit()
    # Não esquecer de atualizar saldo

def Cad_Des():                                             # Irá Cadastrar uma nova despesa
    print('Digite a Despesa')
    dv = float(input('Valor R$: '))
    ddr = input('Data do recebimento: ')
    dd = str(input('Descrição: ').upper())
    dc = str(input('Conta: ').upper())
    dt = str(input('Tipo de Receita: ').upper())

    comando = f"""INSERT INTO DESPESAS(dvalor, ddata, ddescrição, dconta, dtipo)
    VALUES
        ({dv}, '{ddr}', '{dd}', '{dc}', '{dt}')"""
    cursor.execute(comando)
    cursor.commit()
    #Não esquecer de atualizar saldo

def Cad_Con():                                             # Irá Cadastrar uma nova despesa
    print('Digite os dados de sua Conta')
    csaldo = float(input('Valor R$: '))
    ctipo = str(input('Tipo de conta: ').upper())
    cintf = str(input('Instituição Financeira: ').upper())

    comando = f"""INSERT INTO CONTAS(csaldo, ctipo, cintf)
    VALUES
        ({csaldo }, '{ctipo}', '{cintf}')"""
    cursor.execute(comando)
    cursor.commit()

############################################


################## MAIN ####################

Cad_Rec()
Cad_Des()
Cad_Con()

############################################