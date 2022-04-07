import mysql.connector

con = mysql.connector.connect(
    host = 'localhost',
    database = 'estudos',
    user =  'root',
    password = '')

if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ao servidor MySQL versao ", db_info)
    cursor = con.cursor()
    cursor.execute("SELECT DATABASE();")
    linha = cursor.fetchone()
    print("Conectado ao banco de dados: ", linha)
if con.is_connected():
    cursor.close()
    con.close()
    print("Conexao ao MySQL foi encerrada!")