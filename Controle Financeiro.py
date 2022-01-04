
## DB_PubFuture - Pub_1234
##mongodb+srv://DB_PubFuture:<password>@cluster0.1sf5y.mongodb.net/myFirstDatabase?retryWrites=true&w=majority

import pymongo # Biblioteca do banco de dados

cluster = pymongo.MongoClient("mongodb+srv://DB_PubFuture:Pub_1234@cluster0.1sf5y.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")  ## Conecta ao banco de dados

db = cluster.get_database('PubFuture')
collection = db.get_collection('Desafio')
