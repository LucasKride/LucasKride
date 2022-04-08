README

""" Created by: Breno Barbieri """

Project autimation Zabbix and Fresh Service

INSTALAÇÕES NECESSARIAS:
	
	Driver ODBC Driver 17 for SQL Server

	pip install sqlalchemy
	pip install requests
	pip install datetime
	pip install pytz

IMPORTANTE PARA O FUNCIONAMENTO DEVIDO DO SCRIPT:

 => O SUBJECT PRECISA TER O "Resolvido" PARA FUNCIONAR O FECHAMENTO AUTOMATICO DO TICKET

 => NO CORPO DA MESSAGE DE UM RESOLVED, PRECISA SER PASSADO O "ID do problema original: idPassado" EXATAMENTE DESSA FORMA PARA FUNCIONAR O FECHAMENTO AUTOMATICO DO TICKET

 => NÃO ALTERAR OS PARAMETROS PASSADO NA MENSAGEM ENVIADO PELO ZABBIX
	"Id do Alerta: idPassado"

 => PARA A EXECUÇÃO DO SCRIPT DE FORMA DEVIDA, USAR O ARQUIVO "exec.py"


-----------------------------------------------------------------------------------------------------------------------------

Documentação
-----------------------------------------------------------------------------------------------------------------------------
configdb.py
	
	O arquivo "configdb.py" está toda a parte de importação e configuração relacionadas ao banco de dados.

-----------------------------------------------------------------------------------------------------------------------------
	params => Variavel de configuração para acesso ao banco de dados (SQL Server).

	params = urllib.parse.quote_plus("DRIVER={ODBC Driver 17 for SQL Server};" => Driver de conexão
                                 "SERVER=sql-kum-automation.database.windows.net;" => hostname
                                 "DATABASE=db-zabbix-automation;" => database
                                 "UID=admin_kuml;" => username
                                 "PWD=Kumulus@2019xdf") => password 

-----------------------------------------------------------------------------------------------------------------------------
	engine => Variavel responsavel pela conexão onde é usada a variavel "params" que está toda a configuração de conexão do banco. 
-----------------------------------------------------------------------------------------------------------------------------

	@contextmanager => Gerenciador de contexto para que aloque ou libere recursos quando precisos
def session_scope(): => função de conexão + tratamento de erros
    # Session Configuration and Creation
    Session = sessionmaker(bind=engine) 
    session = Session()
    
    # Error handling
    try:
        yield session => yield é um gerador
        session.commit()
    except Exception:
        session.rollback()
        raise  # Exception Main Program Protection (leave it here!)
    finally:
        session.close()






	
	