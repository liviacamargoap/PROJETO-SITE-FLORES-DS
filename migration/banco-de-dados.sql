create database db_site_flores;

use db_site_flores;

create table tb_flores (
	IDflor int auto_increment PRIMARY KEY,
    nome varchar(20) NOT NULL,
    descricao varchar(20),
    preco varchar(20) NOT NULL,
    categoria varchar(20)
);

INSERT INTO tb_flores (IDflor, nome, descricao, preco, categoria)
VALUES  (1, 'buque1', 'descricao-buque1', '10,99', 'buque'),
        (2, 'buque2', 'descricao-buque2', '10,99', 'buque'),
        (3, 'buque3', 'descricao-buque3', '10,99', 'buque'),
        (4, 'buque4', 'descricao-buque4', '10,99', 'buque'),

        (5, 'cesta1', 'descricao-cesta1', '20,99', 'cesta'),
        (6, 'cesta2', 'descricao-cesta2', '20,99', 'cesta'),
        (7, 'cesta3', 'descricao-cesta3', '20,99', 'cesta'),
        (8, 'cesta4', 'descricao-cesta4', '20,99', 'cesta'),

        (9, 'arranjo1', 'descricao-arranjo1', '15,99', 'arranjo'),
        (10, 'arranjo2', 'descricao-arranjo2', '15,99', 'arranjo'),
        (11, 'arranjo3', 'descricao-arranjo3', '15,99', 'arranjo'),
        (12, 'arranjo4', 'descricao-arranjo4', '15,99', 'arranjo');


create table tb_fotos_produto(
	cod_foto int PRIMARY KEY auto_increment,
    IDflor INT, 
    FOREIGN KEY (IDflor) REFERENCES tb_flores(IDflor),
    url_foto1 varchar(250),
    url_foto2 varchar(250),
    url_foto3 varchar(250),
    foto_principal varchar(250)
);

INSERT INTO tb_fotos_produto(foto_principal, url_foto1, url_foto2, url_foto3)
-- arranjo
VALUES  ('https://www.isabelaflores.com/media/catalog/product/a/l/alta-325-2.webp', 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-234-0.webp', 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-27-0.webp', 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-80-0.webp'),
-- buque
('https://www.isabelaflores.com/media/catalog/product/a/l/alta-27-0.webp', 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-234-0.webp', 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-207-1.webp', 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-80-0.webp'),
-- cestas
('https://www.isabelaflores.com/media/catalog/product/a/l/alta-234-0.webp', 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-207-1.webp', 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-80-0.webp', 'https://www.isabelaflores.com/media/catalog/product/a/l/alta-325-2.webp');

create table tb_usuario(
    nome varchar(50) NOT NULL,
    email varchar(50) PRIMARY KEY, 
    telefone int NOT NULL,
    endereco varchar(50) NOT NULL,
    senha varchar(20) NOT NULL
);

create table tb_compra (
	codCompra int auto_increment PRIMARY KEY,
	IDflor INT,
    FOREIGN KEY (IDflor) REFERENCES tb_flores(IDflor)
);