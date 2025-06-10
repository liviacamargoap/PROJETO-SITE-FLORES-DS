from flask import session
from data.conexao import Conexao

class Produtos:
        def obter_produtos(filtro):

                # criando a conexao com banco de dados
                conexao = Conexao.criar_conexao()

                # o cursor é a ponte que vai do python ate o banco de dados
                cursor = conexao.cursor(dictionary = True)

                # criando o SQL que será executado
                # NECESSARIO FAER INNER JOIN ENTRE DOIS SELECT PRA PEGAR AS FOTOS
                
                
                # sql = """SELECT nome, descricao, preco, categoria FROM tb_flores
                #         WHERE categoria = %s """
                sql = """SELECT tb_flores.nome, tb_flores.descricao, tb_flores.preco, tb_flores.categoria, tb_fotos_produto.foto_principal
                        FROM tb_flores
                        INNER JOIN tb_fotos_produto ON tb_flores.IDflor = tb_fotos_produto.IDflor
                        WHERE tb_flores.categoria = %s"""


                valores=(filtro,)

                # executando o comando 
                cursor.execute(sql,valores)

                resultado = cursor.fetchall()

                # fecho a conexao com o banco
                cursor.close()
                conexao.close()

                return resultado


        def obter_todos_produtos():

                # criando a conexao com banco de dados
                conexao = Conexao.criar_conexao()

                # o cursor é a ponte que vai do python ate o banco de dados
                cursor = conexao.cursor(dictionary = True)

                # criando o SQL que será executado
                # NECESSARIO FAER INNER JOIN ENTRE DOIS SELECT PRA PEGAR AS FOTOS
                
                
                # sql = """SELECT nome, descricao, preco, categoria FROM tb_flores
                #         WHERE categoria = %s """
                sql = """SELECT tb_flores.nome, tb_flores.descricao, tb_flores.preco, tb_flores.categoria, tb_fotos_produto.foto_principal
                        FROM tb_flores
                        INNER JOIN tb_fotos_produto ON tb_flores.IDflor = tb_fotos_produto.IDflor"""


                # executando o comando 
                cursor.execute(sql, )

                resultado = cursor.fetchall()

                # fecho a conexao com o banco
                cursor.close()
                conexao.close()

                return resultado
        