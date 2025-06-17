from hashlib import sha256
from flask import session
from data.conexao import Conexao

class Usuario:
        def cadastrar(usuario, telefone, endereco, senha):
                #  criptografando a senha
                senha = sha256(senha.encode()).hexdigest()

                # criando a conexao com banco de dados
                conexao = Conexao.criar_conexao()

                # o cursor é a ponte que vai do python ate o banco de dados
                cursor = conexao.cursor()

                # criando o SQL que será executado
                sql = """INSERT INTO tb_usuario
                        (usuario, telefone, endereco, senha)
                        VALUES
                        (%s, %s, %s, %s)"""
                valores=(usuario, telefone, endereco, senha)

                # executando o comando 
                cursor.execute(sql,valores)

                # confirmo a alteração
                conexao.commit()

                # fecho a conexao com o banco
                cursor.close()
                conexao.close()
    
        def login(usuario, senha):
                #  criptografando a senha
                senha = sha256(senha.encode()).hexdigest()

                # criando a conexao com banco de dados
                conexao = Conexao.criar_conexao()

                # o cursor é a ponte que vai do python ate o banco de dados
                cursor = conexao.cursor(dictionary=True)

                # criando o SQL que será executado
                sql = """SELECT usuario FROM tb_usuario
                        WHERE usuario = %s
                        AND senha = %s """
                valores=(usuario, senha)

                # executando o comando 
                cursor.execute(sql,valores)

                resultado = cursor.fetchone()

                # confirmo a alteração
                conexao.commit()

                # fecho a conexao com o banco
                cursor.close()
                conexao.close()

                if resultado:
                        session["nome_usuario"] = resultado["usuario"]
                        return True
                else:
                        return False
        
        def logoff():
                session.clear()

        