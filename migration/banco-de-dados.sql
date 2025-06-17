create database db_site_flores;

use db_site_flores;

create table tb_categorias (
    id_categoria int auto_increment PRIMARY KEY,
    categoria varchar(20)
);

INSERT INTO tb_categorias (categoria)
VALUES  ('buque'),
        ('cesta'),
        ('arranjo');

create table tb_flores (
    IDflor int auto_increment PRIMARY KEY,
    nome varchar(20) NOT NULL,
    descricao varchar(20),
    preco varchar(20) NOT NULL,
    id_categoria INT NOT NULL,
    FOREIGN KEY (id_categoria) REFERENCES tb_categorias(id_categoria)
);


INSERT INTO tb_flores (IDflor, nome, descricao, preco, id_categoria)
VALUES  (1, 'buque1', 'descricao-buque1', '10,99', 1),
        (2, 'buque2', 'descricao-buque2', '10,99', 1),
        (3, 'buque3', 'descricao-buque3', '10,99', 1),
        (4, 'buque4', 'descricao-buque4', '10,99', 1),

        (5, 'cesta1', 'descricao-cesta1', '20,99', 2),
        (6, 'cesta2', 'descricao-cesta2', '20,99', 2),
        (7, 'cesta3', 'descricao-cesta3', '20,99', 2),
        (8, 'cesta4', 'descricao-cesta4', '20,99', 2),

        (9, 'arranjo1', 'descricao-arranjo1', '15,99', 3),
        (10, 'arranjo2', 'descricao-arranjo2', '15,99', 3),
        (11, 'arranjo3', 'descricao-arranjo3', '15,99', 3),
        (12, 'arranjo4', 'descricao-arranjo4', '15,99', 3);


create table tb_fotos_produto(
    cod_foto int PRIMARY KEY auto_increment,
    IDflor INT, 
    FOREIGN KEY (IDflor) REFERENCES tb_flores(IDflor),
    url_foto1 varchar(250),
    url_foto2 varchar(250),
    url_foto3 varchar(250),
    foto_principal varchar(250)
);

INSERT INTO tb_fotos_produto(IDflor, foto_principal, url_foto1, url_foto2, url_foto3)
-- arranjo
VALUES  (9, 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-325-2.webp', 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-234-0.webp', 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-27-0.webp', 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-80-0.webp'),
        (10, 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-325-2.webp', 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-234-0.webp', 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-27-0.webp', 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-80-0.webp'),
        (11, 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-325-2.webp', 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-234-0.webp', 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-27-0.webp', 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-80-0.webp'),
        (12, 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-325-2.webp', 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-234-0.webp', 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-27-0.webp', 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-80-0.webp'),
-- buque
(1, 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-27-0.webp', 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-234-0.webp', 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-207-1.webp', 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-80-0.webp'),
(2, 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-27-0.webp', 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-234-0.webp', 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-207-1.webp', 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-80-0.webp'),
(3, 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-27-0.webp', 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-234-0.webp', 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-207-1.webp', 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-80-0.webp'),
(4, 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-27-0.webp', 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-234-0.webp', 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-207-1.webp', 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-80-0.webp'),
-- cestas
(5, 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-234-0.webp', 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-207-1.webp', 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-80-0.webp', 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-325-2.webp'),
(6, 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-234-0.webp', 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-207-1.webp', 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-80-0.webp', 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-325-2.webp'),
(7, 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-234-0.webp', 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-207-1.webp', 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-80-0.webp', 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-325-2.webp'),
(8, 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-234-0.webp', 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-207-1.webp', 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-80-0.webp', 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-325-2.webp');

create table tb_usuario(
    usuario varchar(50) PRIMARY KEY NOT NULL,
    telefone int NOT NULL,
    endereco varchar(50) NOT NULL,
    senha varchar(250) NOT NULL
);

create table tb_compra (
    codCompra int auto_increment PRIMARY KEY,
    IDflor INT,
    FOREIGN KEY (IDflor) REFERENCES tb_flores(IDflor)
);


SELECT tb_flores.nome, tb_flores.descricao, tb_flores.preco, tb_flores.id_categoria, tb_fotos_produto.foto_principal
                        FROM tb_flores
                        INNER JOIN tb_fotos_produto ON tb_flores.IDflor = tb_fotos_produto.IDflor;
                        
SELECT id_categoria, categoria from tb_categorias;
SELECT tb_flores.nome, tb_flores.descricao, tb_flores.preco, tb_flores.id_categoria, tb_fotos_produto.foto_principal
                        FROM tb_flores
                        INNER JOIN tb_fotos_produto ON tb_flores.IDflor = tb_fotos_produto.IDflor
                        WHERE tb_flores.id_categoria = 2;