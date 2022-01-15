########## Importanto bibliotecas ##########

import pyodbc               # Biblioteca OBBC para conetar ao banco de dados SQl
import pandas as pd         # Biblioteca Pandas p/ ler o banco de dados
from datetime import date

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



# Função inicial

def Inicial():
    print('\n############################################ Principal ############################################\n')
    exe1 = input('Contas => (C) \n'
                 'Receitas => (R) \n'
                 'Despesas => (D) \n'
                 'Sair => (S) \n'
                 'Digite a opção que deseja executar conforme acima: ').upper()

    while True:
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
    print('\n############################################ Receitas ############################################\n')
    while True:
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
        elif exeR == 'L':
            Lis_Rec()
        elif exeR == 'V':
            Inicial()
        elif exeR == 'S':
            exit()
        else:
            exeR = input('Inválido, tente navamente: ').upper()


def Cad_Rec():                                             # Irá Cadastrar uma nova receita
    print('\n########################################### Nova Receita ###########################################\n')
    print('Digite a Receita')
    rv = float(input('Valor R$: '))
    rdr = input('Data do recebimento no formato 2022-01-31: ')
    rd = str(input('Descrição: ').upper())
    rt = str(input('Tipo de Receita: ').upper())
    ri = str(input('Instituição financeira: ').upper())
    rc = str(input('Tipo de conta: ').upper())
    if hoje >= rdr:                            # Somente atualiza saldo se data da receita for igual ou inferior a atual
        comando = f"""INSERT INTO receitas(rvalor, rdata, rdescrição, rtipo, rintf, rtconta)
            VALUES
                ({rv}, '{rdr}', '{rd}', '{rt}', '{ri}', '{rc}')"""
        cursor.execute(comando)
        cursor.commit()
        Con = f"""SELECT * FROM contas WHERE ctipo = '{rc}' AND cintf = '{ri}'"""
        ConRead = pd.read_sql_query(Con, conexao)
        rvs = pd.Series(ConRead["csaldo"]) + rv
        comando = f"""UPDATE contas SET csaldo={rvs[0]} WHERE cintf='{ri}' AND ctipo='{rc}'"""  # Atualiza o saldo
        cursor.execute(comando)
        cursor.commit()
    else:
        comando = f"""INSERT INTO receitas(rvalor, rdata, rdescrição, rtipo, rintf, rtconta, rfut)
            VALUES
                ({rv}, '{rdr}', '{rd}', '{rt}', '{ri}', '{rc}', {1})"""
        cursor.execute(comando)
        cursor.commit()
        comando = f"""UPDATE contas SET cfut={1} WHERE cintf='{ri}' AND ctipo='{rc}'"""  # Atualiza o saldo
        cursor.execute(comando)
        cursor.commit()
    Inicial()


def Ed_Rec():                                             # Editar as receitas
    print('\n########################################### Editar Receitas ###########################################\n')
    Rec = """SELECT * FROM receitas"""
    listar = pd.read_sql_query(Rec, conexao)
    print(listar)
    esc1 = int(input('Digite o id da receita a ser editada: '))
    esc2 = str(input('Digite o campo que deseja editar: ')).lower()
    esc3 = input('Digite o novo valor: ')
    comando = f"""UPDATE receitas SET {esc2}={esc3} WHERE id={esc1}"""
    cursor.execute(comando)
    cursor.commit()
    if esc2 == 'rvalor':  # Atualizar o saldo somente se editado valor da receita
        varid = listar.query(f'id == {esc1}')
        varval = pd.Series(varid["rvalor"])
        varif = pd.Series(varid["rintf"])
        vartc = pd.Series(varid["rtconta"])
        ind = varid.index
        Con = f"""SELECT * FROM contas WHERE ctipo = '{vartc[ind[0]]}' AND cintf = '{varif[ind[0]]}'"""
        ConRead = pd.read_sql_query(Con, conexao)
        rvs = (pd.Series(ConRead["csaldo"]) - varval[ind[0]]) + int(esc3)
        comando = f"""UPDATE contas SET csaldo={rvs[0]} WHERE cintf='{varif[ind[0]]}' AND ctipo='{vartc[ind[0]]}'"""  # Atualiza o saldo
        cursor.execute(comando)
        cursor.commit()
    Inicial()


def Rem_Rec():                                             # Remover receitas
    print('\n########################################### Remover Receitas ###########################################\n')
    while True:
        exeRR = input('Remover todas => (T) \n'
                      'Especifica => (E) \n' 
                      'Voltar => (V) \n' 
                      'Sair => (S) \n'
                      'Digite uma opção acima: ').upper()
        if exeRR == 'T':
            Rec = """SELECT * FROM receitas"""
            listar = pd.read_sql_query(Rec, conexao)
            for a in range(0, (listar['id'].count())):
                varid = listar.loc[a]
                varval = pd.Series(varid["rvalor"])
                varif = pd.Series(varid["rintf"])
                vartc = pd.Series(varid["rtconta"])
                Con = f"""SELECT * FROM contas WHERE ctipo = '{vartc[0]}' AND cintf = '{varif[0]}'"""
                ConRead = pd.read_sql_query(Con, conexao)
                rvs = pd.Series(ConRead["csaldo"]) - varval[0]
                comando = f"""UPDATE contas SET csaldo={rvs[0]} WHERE cintf='{varif[0]}' AND ctipo='{vartc[0]}'"""  # Atualiza o saldo
                cursor.execute(comando)
                cursor.commit()
            Rem_Rec_SQL = """DELETE FROM receitas"""
            cursor.execute(Rem_Rec_SQL)
            cursor.commit()
            Inicial()
        elif exeRR == 'E':
            Rec = """SELECT * FROM receitas"""
            listar = pd.read_sql_query(Rec, conexao)
            print(listar)
            esc = int(input('Digite o id da receita a ser removida: '))
            escolher = f"""DELETE FROM receitas WHERE id = {esc}"""
            cursor.execute(escolher)
            cursor.commit()
            varid = listar.query(f'id == {esc}')
            varval = pd.Series(varid["rvalor"])
            varif = pd.Series(varid["rintf"])
            vartc = pd.Series(varid["rtconta"])
            ind = varid.index
            Con = f"""SELECT * FROM contas WHERE ctipo = '{vartc[ind[0]]}' AND cintf = '{varif[ind[0]]}'"""
            ConRead = pd.read_sql_query(Con, conexao)
            rvs = pd.Series(ConRead["csaldo"]) - varval[ind[0]]
            comando = f"""UPDATE contas SET csaldo={rvs[0]} WHERE cintf='{varif[ind[0]]}' AND ctipo='{vartc[ind[0]]}'"""  # Atualiza o saldo
            cursor.execute(comando)
            cursor.commit()
            Inicial()
        elif exeRR == 'V':
            Receitas()
        elif exeRR == 'S':
            exit()
        else:
            exeRR = input('Inválido, tente navamente: ').upper()


def Lis_Rec():                                             # Irá Listar as receitas
    print('\n########################################### Filtrar Receitas ###########################################\n')
    while True:
        lisR = input('Todas (A) \n'
                     'Filtrar por Período => (P) \n'
                     'Filtrar por Descrição => (D) \n'
                     'Filtrar por Tipo => (T) \n'
                     'Voltar => (V) \n'
                     'Sair => (S) \n'
                     'Digite a opção que deseja executar conforme acima: ').upper()
        if lisR == 'A':
            Rec = """SELECT * FROM receitas"""
            listar = pd.read_sql_query(Rec, conexao)
            print(listar)
            Inicial()
        elif lisR == 'P':
            perI = input('Digite o período Inicial no formato 2022-01-31: ')
            perF = input('Digite o período Final no formato 2022-01-31:: ')
            Rec = f"""SELECT * FROM receitas WHERE rdata > '{perI}' AND rdata < '{perF}'"""
            listar = pd.read_sql_query(Rec, conexao)
            print(listar)
            Inicial()
        elif lisR == 'D':
            rdes = input('Digite a descrição: ').upper()
            Rec = f"""SELECT * FROM receitas WHERE rdescrição = '{rdes}'"""
            listar = pd.read_sql_query(Rec, conexao)
            print(listar)
            Inicial()
        elif lisR == 'T':
            rtip = input('Digite o tipo de receita: ').upper()
            Rec = f"""SELECT * FROM receitas WHERE rtipo = '{rtip}'"""
            listar = pd.read_sql_query(Rec, conexao)
            print(listar)
            Inicial()
        elif lisR == 'V':
            Receitas()
        elif lisR == 'S':
            exit()
        else:
            lisR = input('Inválido, tente navamente: ').upper()


def at_Rec():
    atua = """SELECT * FROM receitas"""
    atRec = pd.read_sql_query(atua, conexao)
    for a in range(0, len(atRec)):
        fut = atRec.loc[a]
        if fut["rfut"] == True:
            if hoje >= fut["rdata"]:
                Con = f"""SELECT * FROM contas WHERE ctipo = '{fut["rtconta"]}' AND cintf = '{fut["rintf"]}'"""
                ConRead = pd.read_sql_query(Con, conexao)
                rvs = pd.Series(ConRead["csaldo"]) + fut["rvalor"]
                comando = f"""UPDATE contas SET csaldo={rvs[0]} WHERE ctipo = '{fut["rtconta"]}' AND cintf = '{fut["rintf"]}' """  # Atualiza o saldo
                cursor.execute(comando)
                cursor.commit()
                comando = f"""UPDATE receitas SET rfut={0} WHERE id = '{fut["id"]}' """  # Atualiza o saldo
                cursor.execute(comando)
                cursor.commit()


# Funções referentes as Despesas


def Despesas():
    print('\n############################################ Despesas ############################################\n')
    while True:
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
            Inicial()
        elif exeD == 'S':
            exit()
        else:
            exeD = input('Inválido, tente navamente: ').upper()


def Cad_Des():                                             # Irá Cadastrar uma nova despesa
    print('\n########################################### Nova Despesa ###########################################\n')
    print('Digite a Despesa')
    dv = float(input('Valor R$: '))
    ddr = input('Data do Pagamento no formato 2022-01-31: ')
    dd = str(input('Descrição: ').upper())
    dt = str(input('Tipo de Despesa: ').upper())
    di = str(input('Instituição financeira: ').upper())
    dc = str(input('Tipo de conta: ').upper())
    if hoje >= ddr:                            # Somente atualiza saldo se data da despesa for igual ou inferior a atual
        comando = f"""INSERT INTO despesas(dvalor, ddata, ddescrição, dtipo, dintf, dtconta)
            VALUES
                ({dv}, '{ddr}', '{dd}', '{dt}', '{di}', '{dc}')"""
        cursor.execute(comando)
        cursor.commit()
        Con = f"""SELECT * FROM contas WHERE ctipo = '{dc}' AND cintf = '{di}'"""
        ConRead = pd.read_sql_query(Con, conexao)
        rvs = pd.Series(ConRead["csaldo"]) - dv
        comando = f"""UPDATE contas SET csaldo={rvs[0]} WHERE cintf='{di}' AND ctipo='{dc}'"""        #Atualiza o saldo
        cursor.execute(comando)
        cursor.commit()
    else:
        comando = f"""INSERT INTO despesas(dvalor, ddata, ddescrição, dtipo, dintf, dtconta, dfut)
                    VALUES
                        ({dv}, '{ddr}', '{dd}', '{dt}', '{di}', '{dc}', {1})"""
        cursor.execute(comando)
        cursor.commit()
        comando = f"""UPDATE contas SET cfut={1} WHERE cintf='{di}' AND ctipo='{dc}'"""
        cursor.execute(comando)
        cursor.commit()
    Inicial()


def Ed_Des():                                             # Editar  Despesas
    print('\n########################################### Editar Despesas ###########################################\n')
    Des = """SELECT * FROM despesas"""
    listar = pd.read_sql_query(Des, conexao)
    print(listar)
    esc1 = int(input('Digite o id da despesa ser editada: '))
    esc2 = str(input('Digite o campo que deseja editar: ')).lower()
    esc3 = input('Digite o novo valor: ')
    comando = f"""UPDATE despesas SET {esc2}={esc3} WHERE id='{esc1}'"""
    cursor.execute(comando)
    cursor.commit()
    if esc2 == 'dvalor':  # Atualizar o saldo somente se editado valor da despesa
        varid = listar.query(f'id == {esc1}')
        varval = pd.Series(varid["dvalor"])
        varif = pd.Series(varid["dintf"])
        vartc = pd.Series(varid["dtconta"])
        ind = varid.index
        Con = f"""SELECT * FROM contas WHERE ctipo = '{vartc[ind[0]]}' AND cintf = '{varif[ind[0]]}'"""
        ConRead = pd.read_sql_query(Con, conexao)
        rvs = (pd.Series(ConRead["csaldo"]) + varval[ind[0]]) - int(esc3)
        comando = f"""UPDATE contas SET csaldo={rvs[0]} WHERE cintf='{varif[ind[0]]}' AND ctipo='{vartc[ind[0]]}'"""  # Atualiza o saldo
        cursor.execute(comando)
        cursor.commit()
    Inicial()


def Rem_Des():                                             # Remover Despesas
    print('\n########################################### Remover Despesas ###########################################\n')
    exeRD = input('Remover todas => (T) \n'
                  'Especifica => (E) \n'
                  'Voltar => (V) \n'
                  'Sair => (S) \n'
                  'Digite uma opção acima: ').upper()

    if exeRD == 'T':
        Des = """SELECT * FROM despesas"""
        listar = pd.read_sql_query(Des, conexao)
        for a in range(0, (listar['id'].count())):
            varid = listar.loc[a]
            varval = pd.Series(varid["dvalor"])
            varif = pd.Series(varid["dintf"])
            vartc = pd.Series(varid["dtconta"])
            Con = f"""SELECT * FROM contas WHERE ctipo = '{vartc[0]}' AND cintf = '{varif[0]}'"""
            ConRead = pd.read_sql_query(Con, conexao)
            rvs = pd.Series(ConRead["csaldo"]) + varval[0]
            comando = f"""UPDATE contas SET csaldo={rvs[0]} WHERE cintf='{varif[0]}' AND ctipo='{vartc[0]}'"""  # Atualiza o saldo
            cursor.execute(comando)
            cursor.commit()
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
        varid = listar.query(f'id == {esc}')
        varval = pd.Series(varid["dvalor"])
        varif = pd.Series(varid["dintf"])
        vartc = pd.Series(varid["dtconta"])
        ind = varid.index
        Con = f"""SELECT * FROM contas WHERE ctipo = '{vartc[ind[0]]}' AND cintf = '{varif[ind[0]]}'"""
        ConRead = pd.read_sql_query(Con, conexao)
        rvs = pd.Series(ConRead["csaldo"]) + varval[ind[0]]
        comando = f"""UPDATE contas SET csaldo={rvs[0]} WHERE cintf='{varif[ind[0]]}' AND ctipo='{vartc[ind[0]]}'"""  # Atualiza o saldo
        cursor.execute(comando)
        cursor.commit()
        Inicial()
    elif exeRD == 'V':
        Despesas()
    elif exeRD == 'S':
        exit()
    else:
        exeRD = input('Inválido, tente navamente: ').upper()


def Lis_Des():                                             # Listar as Despesas
    print('\n########################################### Filtrar Despesas ###########################################\n')
    while True:
        lisD = input('Todas (A) \n'
                     'Por Período (P) \n'
                     'Filtrar por Descrição => (D) \n'
                     'Filtrar por Tipo => (T) \n'
                     'Voltar => (V) \n'
                     'Sair => (S) \n'
                     'Digite a opção que deseja executar conforme acima: ').upper()
        if lisD == 'A':
            Des = """SELECT * FROM despesas"""
            listar = pd.read_sql_query(Des, conexao)
            print(listar)
            Inicial()
        elif lisD == 'P':
            perI = input('Digite o período Inicial no formato 2022-01-31: ')
            perF = input('Digite o período Final no formato 2022-01-31: ')
            Des = f"""SELECT * FROM despesas WHERE ddata > '{perI}' AND ddata < '{perF}' """
            listar = pd.read_sql_query(Des, conexao)
            print(listar)
            Inicial()
        elif lisD == 'D':
            ddes = input('Digite a descrição: ').upper()
            Des = f"""SELECT * FROM receitas WHERE ddescrição = '{ddes}'"""
            listar = pd.read_sql_query(Des, conexao)
            print(listar)
            Inicial()
        elif lisD == 'T':
            dtip = input('Digite o tipo de despesa: ').upper()
            Des = f"""SELECT * FROM receitas WHERE dtipo = '{dtip}'"""
            listar = pd.read_sql_query(Des, conexao)
            print(listar)
            Inicial()
        elif lisD == 'V':
            Despesas()
        elif lisD == 'S':
            exit()
        else:
            lisR = input('Inválido, tente navamente: ').upper()


def at_Des():
    atua = """SELECT * FROM despesas"""
    atDes = pd.read_sql_query(atua, conexao)
    for a in range(0, len(atDes)):
        fut = atDes.loc[a]
        if fut["dfut"] == True:
            if hoje >= fut["ddata"]:
                Con = f"""SELECT * FROM contas WHERE ctipo = '{fut["dtconta"]}' AND cintf = '{fut["dintf"]}'"""
                ConRead = pd.read_sql_query(Con, conexao)
                rvs = pd.Series(ConRead["csaldo"]) - fut["dvalor"]
                comando = f"""UPDATE contas SET csaldo={rvs[0]} WHERE ctipo = '{fut["dtconta"]}' AND cintf = '{fut["dintf"]}' """  # Atualiza o saldo
                cursor.execute(comando)
                cursor.commit()
                comando = f"""UPDATE receitas SET dfut={0} WHERE id = '{fut["id"]}' """  # Atualiza o saldo
                cursor.execute(comando)
                cursor.commit()


# Funções referentes as Contas

def Contas():
    print('\n############################################ Contas ############################################\n')
    while True:
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
            Inicial()
        elif exeC == 'S':
            exit()
        else:
            exeC = input('Inválido, tente navamente: ').upper()

def Cad_Con():                                             # Cadastrar Contas
    print('\n########################################### Nova Conta ###########################################\n')
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


def Ed_Con():                                             # Editar Contas
    print('\n########################################### Editar Contas ###########################################\n')
    Con = """SELECT * FROM contas"""
    listar = pd.read_sql_query(Con, conexao)
    print(listar)
    esc1 = int(input('Digite o id da conta a ser editada: '))
    esc2 = str(input('Digite o campo que deseja editar: ')).lower()
    esc3 = input('Digite o novo valor: ')
    comando = f"""UPDATE contas SET {esc2}={esc3} WHERE id='{esc1}'"""
    cursor.execute(comando)
    cursor.commit()
    Inicial()


def Rem_Con():                                             # Remover Contas
    print('\n########################################### Remover Contas ###########################################\n')
    while True:
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


def Lis_Con():                                             # Irá Listar as Contas
    print('\n########################################### Filtrar Contas ###########################################\n')
    Con = """SELECT * FROM contas"""
    listar = pd.read_sql_query(Con, conexao)
    print(listar)
    Inicial()


def Tra_Con():                                             # Transferir saldo entre contas
    print('\n####################################### Transferência de Saldo #######################################\n')
    Con = f"""SELECT * FROM contas"""
    ConRead = pd.read_sql_query(Con, conexao)
    print(ConRead)
    ctra = float(input('Digite o valor a transferir: '))
    ctifi = input('Digite a Intituição financeira de origem: ').upper()
    ctci = input('Digite a conta de origem: ').upper()
    ctifo = input('Digite a Intituição financeira de destino: ').upper()
    ctco = input('Digite a conta de destino: ').upper()
    varifi = ConRead.query(f"""cintf == '{ctifi}' and ctipo == '{ctci}'""")
    csali = pd.Series(varifi["csaldo"]) - ctra
    ind = csali.index
    Con = f"""UPDATE contas SET csaldo={csali[ind[0]]} WHERE cintf='{ctifi}' AND ctipo='{ctci}'"""
    cursor.execute(Con)
    cursor.commit()
    varifo = ConRead.query(f"""cintf == '{ctifo}' and ctipo == '{ctco}'""")
    csalo = pd.Series(varifo["csaldo"]) + ctra
    ind = csalo.index
    Con = f"""UPDATE contas SET csaldo={csalo[ind[0]]} WHERE cintf='{ctifo}' AND ctipo='{ctco}'"""
    cursor.execute(Con)
    cursor.commit()
    print('Transferencia finalizada')
    Inicial()


def Lit_Con():                                             #Apresenta saldo total
    print('\n############################################ Saldo ############################################\n')

    Con = f"""SELECT SUM(csaldo) from contas"""
    ConRead = pd.read_sql_query(Con, conexao)
    csaldo = ConRead.loc[0]
    print(f'Seu saldo total é de: R$ {csaldo[0]}')
    Inicial()



############################################


################## MAIN ####################

hoje = str(date.today())


Con = """SELECT * FROM contas"""        #Coferir se a valor "futuro" a atualizar
contas = pd.read_sql_query(Con, conexao)
for a in range(0, len(contas)):
    fut = contas.loc[a]
    if fut["cfut"] == True:
    at = True

if at == True:
    for a in range(0, 1):
        if a == 0:
            at_Rec()
        else:
            at_Des()
    Rec = """SELECT COUNT(*) FROM receitas WHERE rfut=1;"""
    RecFut = pd.read_sql_query(Rec, conexao)
    rec = pd.Series(RecFut[""])
    ind = RecFut.index
    Des = """SELECT COUNT(*) FROM despesas WHERE dfut=1;"""
    DesFut = pd.read_sql_query(Des, conexao)
    des = pd.Series(DesFut[""])
    ind = DesFut.index
    if des[ind[0]]==0 and rec[ind[0]]==0:
        con = f"""UPDATE contas SET cfut={0}"""
    cursor.execute(Con)
    cursor.commit()
Inicial()






############################################

