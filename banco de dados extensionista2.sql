/*Criação do banco de dados.*/
CREATE DATABASE extensionista2;

/*Comando para utilizar o banco de dados extensionist2.*/
USE extensionista2;

/*Criação de 3 tabelas com colunas, um auto incremento, constraint e chave primária em cada uma.*/
CREATE TABLE Perguntas( cod_perguntas int(3) auto_increment, pergunta1 char , pergunta2 char  , pergunta3 char, constraint pk_perguntas primary key(cod_perguntas) );
CREATE TABLE Cadastro( cod_cadastro int(3) auto_increment, nome varchar(100) not null, endereco varchar(100) , telefone bigint, constraint pk_cadastro  primary key(cod_cadastro));
CREATE TABLE Argumento( cod_argumento int(3) auto_increment, aceitabilidade char , argumento varchar(100), constraint pk_argumento  primary key(cod_argumento) );

/*Criação da tabela Menu a qual receberá as chaves estrangeiras das respectivas tabelas criadas anteriormente.*/
CREATE TABLE Menu(cod_menu int(3) auto_increment primary key,cod_perguntas int(3) ,cod_cadastro int(3), cod_argumento int(3),constraint fk_perguntas foreign key(cod_perguntas) references Perguntas(cod_perguntas) 
, constraint fk_cadastro  foreign key(cod_cadastro) references Cadastro(cod_cadastro), constraint fk_argumento  foreign key(cod_argumento) 
references Argumento(cod_argumento));







