import pymongo

#Conexão com o cliet
client = pymongo.MongoClient("mongodb://localhost:27017/")

#Acesso ou criação do novo banco
db = client.get_database("NomeDoBanco")

#Acesso ou criação da nova collection
collections = db.get_collection("NomeDaCollection")

#Insercao dentro da collection
collections.insert_many(
    [
        {"nome": "PlaceHolderNome"},
        {"email": "PlaceHolderEmail"},
        {"endereco": "PlaceHolderEndereco"},
    ]
)

#Leitura da collection
for doc in collections.find():
    print(doc)

#Leitura filtrada
for doc in collections.find({"nome": "PlaceHolderNome"}):
    print(doc)

#Update
collections.update_one(
    {"endereco": "PlaceHolderEndereco"},
    {"$set": {"endereco": "PlaceHolderEnderecoNovo"}}
)

#Delete
collections.delete_many(
    {"email": "PlaceHolderEmail"}
)

#Leitura da collection
for doc in collections.find():
    print(doc)

#Leitura dos bancos de dados existentes
for db_name in client.list_database_names():
    print(db_name)

#Caso as alteracoes nao sejam refletidas no seu MongoDB Compass, clicar no botao de refresh ao lado da lista de databases.
