import sqlite3 as lite

#criando connection
con = lite.connect('dados.db')

#criando tabela
with con:
    cur=con.cursor()
    cur.execute("CREATE TABLE inventario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT,local TEXT,descricao TEXT, marca TEXT, data_compra DATE, valor_compra DECIMAL, serie TEXT, imagem TEXT)")