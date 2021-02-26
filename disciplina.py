from pymongo import ReturnDocument

if __name__ == '__main__':
    pass
import pymongo


def createDB():
    nome_disc = input("insira o nome da disciplina\n")
    nome_prof = input("Insira o nome do professor\n")
    return {"nomeDisciplina": nome_disc, "nomeProfessor": nome_prof}


def readDB(database):
    query = input("por favor digite o nome da disciplina a ser consultada\n")
    return database.find_one({"nomeDisciplina": query})



def updateDB(database):
    print ("Atualizando disciplina")
    disciplina.find_one_and_update(readDB(database), {"$set": createDB()}, return_document=ReturnDocument.AFTER)


def deleteDB(database):
    query = input("por favor digite o nome da disciplina a ser deletada\n")
    return database.delete_one({"nomeDisciplina": query})

def printAll(database):
    printer = database.find({})
    for item in printer:
        print(item)


client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
db = client["bd3"]
disciplina = db["disciplina"]


ListDisc = list()
db.drop_collection("disciplina")
ListDisc.append({"nomeDisciplina" : "Circuitos", "nomeProfessor" : "Lucas Oliveira"})
ListDisc.append({"nomeDisciplina" : "Fisica 1", "nomeProfessor" : "Fernanda Nodari"})
ListDisc.append({"nomeDisciplina" : "Calculo", "nomeProfessor" : "Jose da Silva"})
ListDisc.append({"nomeDisciplina" : "Computaçao 1", "nomeProfessor" : "Jorge Habib"})
ListDisc.append({"nomeDisciplina" : "Estatistica", "nomeProfessor" : "Carlos dos Santos"})
ListDisc.append({"nomeDisciplina" : "Engenharia de Software", "nomeProfessor" : "Gil Brasil"})
disciplina.insert_many(ListDisc)

"""
printAll(disciplina)
disciplina.insert_one(createDB())
print(readDB(disciplina))
updateDB(disciplina)
deleteDB(disciplina)
print(readDB(disciplina))
"""
