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

def Inicial():
    exe1 = input('Contas => (C) \n'
                 'Receitas => (R) \n'
                 'Despesas => (D) \n'
                 'Sair => (S) \n'
                 'Digite a opção que deseja executar conforme acima: ').upper()

    if exe1 == 'C':
        Contas()
    elif exe1 == 'R':
        Receitas()
    elif exe1 == 'D':
        Despesas()
    elif exe1 == 'S':
        exit()
    else:
        exe1 = input('Inválido, tente navamente: ').upper()


# Funções referentes as Receitas

def Receitas():
    exeR = input('Nova => (N) \n'
                 'Editar=> (E) \n'
                 'Remover => (R) \n'
                 'Listar => (L) \n'
                 'Voltar => (V) \n'
                 'Sair => (S) \n'
                 'Digite a opção que deseja executar conforme acima: ').upper()

    if exeR == 'N':
        Cad_Rec()
    elif exeR == 'E':
        Ed_Rec()
    elif exeR == 'R':
        Rem_Rec()
    elif exeR == 'V':
        v = 'Voltar' #Fazer função
    elif exeR == 'S':
        exit()
    else:
        exeR = input('Inválido, tente navamente: ').upper()


def Cad_Rec():                                             # Irá Cadastrar uma nova receita
    print('Digite a Receita')
    rv = float(input('Valor R$: '))
    rdr = input('Data do recebimento: ')
    rd = str(input('Descrição: ').upper())
    rc = str(input('Conta: ').upper())
    rt = str(input('Tipo de Receita: ').upper())
    comando = f"""INSERT INTO receitas(rvalor, rdata, rdescrição, rconta, rtipo)
    VALUES
        ({rv}, '{rdr}', '{rd}', '{rc}', '{rt}')"""
    cursor.execute(comando)
    cursor.commit()
    Inicial()
    # Não esquecer de atualizar saldo


def Ed_Rec():                                             # Editar as receitas
    '''conexao = pyodbc.connect(dados_conexao)
    cursor = conexao.cursor()
    Rec = """SELECT * FROM RECEITAS"""
    listar = pd.read_sql_query(Rec, conexao)
    esc = str(input('Digite a despesa a ser removida: ')).upper()
    editar = f"""UPDATE DESPESAS SET ddescrição='{esc}' WHERE ddescrição='nubanK'"""
    esc1 = str(input('Digite a despesa a editada: ')).upper()
    esc2 = input('Digite o campo que a editado: ')
    esc3 = input('Digite o o novo valor: ')
    escolher = f"""UPDATE DESPESAS SET {esc2}={esc3} WHERE {ddescrição}='{esc2}'"""
    print(escolher)
    cursor.execute(escolher)'''


def Rem_Rec():                                             # Remover receitas
    exeRR = input('Remover todas => (T) \n'
                  'Especifica => (E) \n' 
                  'Voltar => (V) \n' 
                  'Sair => (S) \n'
                  'Digite uma opção acima: ').upper()

    if exeRR == 'T':
        Rem_Rec_SQL = """DELETE FROM receitas"""
        cursor.execute(Rem_Rec_SQL)
        cursor.commit()
        Inicial()
    elif exeRR == 'E':
        conexao = pyodbc.connect(dados_conexao)
        cursor = conexao.cursor()
        Rec = """SELECT * FROM receitas"""
        listar = pd.read_sql_query(Rec, conexao)
        print(listar)
        esc = int(input('Digite o id da receita a ser removida: '))
        escolher = f"""DELETE FROM receitas WHERE id = ''"""
        cursor.execute(escolher)
        cursor.commit()
        Inicial()
        #NÃO ESQUECER DE ATUALIZAR O SALDO
    elif exeRR == 'V':
        Receitas()
    elif exeRR == 'S':
        exit()
    else:
        exeRR = input('Inválido, tente navamente: ').upper()


def Lis_Rec():                                             # Irá Listar as receitas
   ''' sql_Rec = """SELECT * FROM RECEITAS"""
    Rec = pd.read_sql_query(sqlEXEC, conexao)
    return Rec'''



# Funções referentes as Despesas


def Despesas():
    exeD = input('Nova => (N) \n'
                 'Editar=> (E) \n'
                 'Remover => (R) \n'
                 'Listar => (L) \n'
                 'Voltar => (V) \n'
                 'Sair => (S) \n'
                 'Digite a opção que deseja executar conforme acima: ').upper()

    if exeD == 'N':
        Cad_Des()
    elif exeD == 'E':
        Ed_Des()
    elif exeD == 'R':
        Rem_Des()
    elif exeD == 'L':
        Lis_Des()
    elif exeD == 'V':
        v = 'Voltar' #Fazer função
    elif exeD == 'S':
        exit()
    else:
        exeD = input('Inválido, tente navamente: ').upper()


def Cad_Des():                                             # Irá Cadastrar uma nova despesa
    print('Digite a Despesa')
    dv = float(input('Valor R$: '))
    ddr = input('Data do Pagamento: ')
    dd = str(input('Descrição: ').upper())
    dc = str(input('Conta: ').upper())
    dt = str(input('Tipo de Despesa: ').upper())
    comando = f"""INSERT INTO despesas(dvalor, ddata, ddescrição, dconta, dtipo)
    VALUES
        ({dv}, '{ddr}', '{dd}', '{dc}', '{dt}')"""
    cursor.execute(comando)
    cursor.commit()
    Inicial()
    #Não esquecer de atualizar saldo


def Ed_Des():                                             # Irá Editar uma Despesa
    a = 'ok'


def Rem_Des():                                             # Remover Despesas
    exeRD = input('Remover todas => (T) \n'
                  'Especifica => (E) \n'
                  'Voltar => (V) \n'
                  'Sair => (S) \n'
                  'Digite uma opção acima: ').upper()

    if exeRD == 'T':
        Rem_Des_SQL = """DELETE FROM despesas"""
        cursor.execute(Rem_Des_SQL)
        cursor.commit()
        Inicial()
    elif exeRD == 'E':
        Des = """SELECT * FROM despesas"""
        listar = pd.read_sql_query(Des, conexao)
        print(listar)
        esc = int(input('Digite o id da despesa a ser removida: '))
        escolher = f"""DELETE FROM DESPESAS WHERE id = {esc}"""
        cursor.execute(escolher)
        cursor.commit()
        Inicial()
        # NÃO ESQUECER DE ATUALIZAR O SALDO
    elif exeRD == 'V':
        Despesas()
    elif exeRD == 'S':
        exit()
    else:
        exeRD = input('Inválido, tente navamente: ').upper()


def Lis_Des():                                             # Irá Listar as Despesa
    a = 'ok'



# Funções referentes as Contas

def Contas():
    exeC = input('Nova => (N) \n'
                 'Editar=> (E) \n'
                 'Remover => (R) \n'
                 'Listar => (L) \n'
                 'Transferir => (T) \n'
                 'Listar Saldos=> (LS) \n'
                 'Voltar => (V) \n'
                 'Sair => (S) \n'
                 'Digite a opção que deseja executar conforme acima: ').upper()

    if exeC == 'N':
        Cad_Con()
    elif exeC == 'E':
        Ed_Con()
    elif exeC == 'R':
        Rem_Con()
    elif exeC == 'L':
        Lis_Con()
    elif exeC == 'T':
        Tra_Con()
    elif exeC == 'LS':
        Lit_Con()
    elif exeC == 'V':
        v = 'Voltar' #Fazer função
    elif exeC == 'S':
        exit()
    else:
        exeC = input('Inválido, tente navamente: ').upper()

def Cad_Con():                                             # Irá Cadastrar uma nova despesa
    print('Digite os dados de sua Conta')
    csaldo = float(input('Valor R$: '))
    ctipo = str(input('Tipo de conta: ').upper())
    cintf = str(input('Instituição Financeira: ').upper())

    comando = f"""INSERT INTO contas(csaldo, ctipo, cintf)
    VALUES
        ({csaldo }, '{ctipo}', '{cintf}')"""
    cursor.execute(comando)
    cursor.commit()
    Inicial()


def Ed_Con():                                             # Irá Editar uma Despesa
    a = 'ok'


def Rem_Con():                                             # Remover Contas
    exeRC = input('Remover todas => (T) \n'
                  'Especifica => (E) \n'
                  'Voltar => (V) \n'
                  'Sair => (S) \n'
                  'Digite uma opção acima: ').upper()

    if exeRC == 'T':
        Rem_Con_SQL = """DELETE FROM contas"""
        cursor.execute(Rem_Con_SQL)
        cursor.commit()
        Inicial()
    elif exeRC == 'E':
        Con = """SELECT * FROM contas"""
        listar = pd.read_sql_query(Con, conexao)
        print(listar)
        esc = int(input('Digite o id da conta a ser removida: '))
        escolher = f"""DELETE FROM CONTAS WHERE id = {esc}"""
        cursor.execute(escolher)
        cursor.commit()
        Inicial()
        # NÃO ESQUECER DE ATUALIZAR O SALDO
    elif exeRC == 'V':
        Contas()
    elif exeRC == 'S':
        exit()
    else:
        exeRD = input('Inválido, tente navamente: ').upper()


def Lis_Con():                                             # Irá Listar as Despesa
    a = 'ok'


def Tra_Con():                                             # Irá Editar uma Despesa
    a = 'ok'


def Lit_Con():                                             # Irá Remover uma Despesa
    a = 'ok'


############################################


################## MAIN ####################


Inicial()

'''Des = """SELECT * FROM DESPESAS"""
listar = pd.read_sql_query(Des, conexao)
print(listar)'''



#UPDATE estudantes SET nome = 'Rafael Rodrigues Maia' WHERE id = 23;

############################################


