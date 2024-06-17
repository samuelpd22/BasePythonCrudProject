import sqlite3 as lite

con = lite.connect('dados.db')

#______________________________________ CRUD_________________________________________


#inserir dados POST
def inserir_dados(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO inventario(nome ,local , descricao ,marca, data_compra,valor_compra,serie,imagem) VALUES(?,?,?,?,?,?,?,?)"
        cur.execute(query,i)



#Atualizar dados PUT
def atualizar_dados(i):
    with con:
        cur = con.cursor()
        query = "UPDATE inventario SET nome=? ,local=? , descricao=? ,marca=?, data_compra=?,valor_compra=?,serie=?,imagem=? WHERE id=? "
        cur.execute(query,i)


#DELETAR DADOS por ID
def deletar_dados(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM inventario WHERE  id=?"
        cur.execute(query,i)



#Ver dados GET All
def ver_todos_dados():
    ver_dados = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM inventario"
        cur.execute(query)

        #fetchall PEGAR TUDO
        filas = cur.fetchall()
        for dadosfila in filas:
            ver_dados.append(dadosfila)
    return ver_dados


#Ver item por ID
def ver_item_porid(id):
    ver_dados_individual = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM inventario WHERE id=?"
        cur.execute(query,id)

        #fetchall PEGAR TUDO
        filas = cur.fetchall()
        for dadosfila in filas:
            ver_dados_individual.append(dadosfila)







    




