import mysql.connector

con = mysql.connector.connect(
    host = 'localhost',
    database = 'estudos',
    user =  'root',
    password = '')

if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ao servidor MySQL versao ", db_info) #daqui para baixo pode ter outras linhas de programa como adicionar remover linkar etcetc
    cursor = con.cursor()
    cursor.execute("SELECT DATABASE();")
    linha = cursor.fetchone()
    print("Conectado ao banco de dados: ", linha)
if con.is_connected(): #exemplo de como encerrar a coneccao com do MySQL com o phyton
    cursor.close()
    con.close()
    print("Conexao ao MySQL foi encerrada!")