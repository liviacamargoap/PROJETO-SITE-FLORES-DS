from hashlib import sha256
from flask import session
from data.conexao import Conexao

class Usuario:
        def cadastrar(nome, email, telefone, endereco, senha):
                #  criptografando a senha
                senha = sha256(senha.encode()).hexdigest()

                # criando a conexao com banco de dados
                conexao = Conexao.criar_conexao()

                # o cursor é a ponte que vai do python ate o banco de dados
                cursor = conexao.cursor()

                # criando o SQL que será executado
                sql = """INSERT INTO tb_usuario
                        (nome, email, telefone, endereco, senha)
                        VALUES
                        (%s, %s, %s, %s, %s)"""
                valores=(nome, email, telefone, endereco, senha)

                # executando o comando 
                cursor.execute(sql,valores)

                # confirmo a alteração
                conexao.commit()

                # fecho a conexao com o banco
                cursor.close()
                conexao.close()
    
        def login(email, senha):
                #  criptografando a senha
                senha = sha256(senha.encode()).hexdigest()

                # criando a conexao com banco de dados
                conexao = Conexao.criar_conexao()

                # o cursor é a ponte que vai do python ate o banco de dados
                cursor = conexao.cursor(dictionary=True)

                # criando o SQL que será executado
                sql = """SELECT email, senha FROM tb_usuario
                        WHERE email = %s
                        AND senha = %s """
                valores=(email, senha)

                # executando o comando 
                cursor.execute(sql,valores)

                resultado = cursor.fetchone()

                # confirmo a alteração
                conexao.commit()

                # fecho a conexao com o banco
                cursor.close()
                conexao.close()

                # if resultado:
                #         session["email"] = resultado["email"]
                #         session["nome_usuario"] = resultado["senha"]
                #         return True
                # else:
                #         return False
        
        def logoff():
                session.clear()

        