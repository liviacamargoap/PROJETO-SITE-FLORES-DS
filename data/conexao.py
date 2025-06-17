import mysql.connector
class Conexao: 
    def criar_conexao():
        conexao = mysql.connector.connect(
            host = "localhost",
            port = 3306,
            user = "root",
            password = "root",
            database = "db_site_flores"
    )
        return conexao
    
    # def criar_conexao():
    #     conexao = mysql.connector.connect(
    #         host = "projeto-site-flores-db-projeto-site-flores.c.aivencloud.com",
    #         port = 28977,
    #         user = "avnadmin",
    #         password = "AVNS_V1fn2-jAXLaPIF5xW6h",
    #         database = "defaultdb"
    # )
    #     return conexao
    
