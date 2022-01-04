import pymongo # Biblioteca do banco de dados

cluster = pymongo.MongoClient("mongodb+srv://DB_PubFuture:Pub_1234@cluster0.1sf5y.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")  ## Conecta ao banco de dados
## DB_PubFuture - Pub_1234

db = cluster.get_database('PubFuture')
collection_con = db.get_collection('Contas')                # Conecta ao DB de contas
collection_des = db.get_collection('Despesas')             # Conecta ao DB de despesas
collection_rec = db.get_collection('Receitas')             # Conecta ao DB de receitas


def Cad_Rec():                                             # Irá Cadastrar uma nova receita
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

    '''rv = valor
    rdr = dataRecebimento
    rd = descrição
    rc = conta
    rt = tipoReceita (salário, presente, prêmio, outros)'''


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

    '''dv = valor
    ddr = data do Recebimento
    dd = descrição
    dc = conta
    dt = tipo da Despesa (salário, presente, prêmio, outros)'''


Cad_Des()
Cad_Rec()
