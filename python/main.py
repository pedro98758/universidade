from modules.aluno import Aluno
from modules.mysql import MySQL
banco = MySQL()
banco.connect()
aluno = Aluno(
    "José Maria", 
    "jose.maria@gmail.com",
    "98765432110",
    "0319400289224",
    "Rua Paineiras, Eldorado, 3000"
    )
query = aluno.cadastrar()
# print(query)
banco.execute_query(query)
banco.disconnect()