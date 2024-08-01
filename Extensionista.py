import mysql.connector
#Conecta o mysql com o python.
conexao=mysql.connector.connect(host='localhost',
                                database='extensionista2',
                                user='root',
                                password='password')#Tutoria ao corrigir deverá logar com seu host e senha. o database extensionista2 deverá ser criado antes no mysql.
#Variável cursor recebe conexao(conecta python com o mysql) aplicando o comando cursor
cursor=conexao.cursor()

#Ao conectar com sucesso, imprime a mensagem do print abaixo.
if conexao.is_connected():
    print('Banco de dados conectado!')

def cadastro():# Ao selecionar a opção cadastro como uma das opções que aparece no menu abrirá esta função.
  while True:# Laço de repetição para continuar a aderir cadastro enquanto for preciso.

     try:#Comando para tentar executar, utilizado para tratar erro de exceção(em conjunto).

         #Perguntas que aparecerão para que o usuário digite seus dados.
        name=str(input('Digite o nome do indivíduo:'))
        address=str(input('Digite o endereço do indivíduo:'))
        phonenumber = int(input('Digite o telefone do indivíduo:'))

        if phonenumber:#Condição para que grave no banco de dados apenas quando os valores da variável phonenumber forem inteiros.

         # A variável comando recebe comandos de INSERT do mysql, sendo aderidos os valores referente aos inputs das perguntas de cima( no mysql entra como values nas colunas nome,endereco e telefone respectivamentes).
         comando = f"""INSERT INTO Cadastro(nome,endereco,telefone) VALUES('{name}','{address}','{phonenumber}')"""
         global cursor#Traz a variável cursor do escorpo global para que possa ser utilizada na conexão com o banco de dados.
         cursor.execute(comando)  # Executa a ação INSERT contido na variável comando no banco de dado do mysql.
         conexao.commit()  # Comando que possibilita editar o banco de dados, utilizado para gravar e alterar valores.


     except ValueError:#Se caso acontecer um erro de não digitar valor int no input da variável phonenumber.
         print("Digite somente números para cadastro do contato telefônico.")
         continue#Volta para o laço de repetição.

     def repetirPergunta():#utilizado para retornar as perguntas de inputs da função cadastro, caso o usuário desejar.

         while True:

             A=input('Deseja realizar mais cadastros?(S/N)')#Pergunta para averiguar se deseja continuar cadastrando novamente ou sair.

             if A.upper()=='S':
                cadastro()#Se 's' ou 'S' retorna no inicio para cadastrar mais(novamente a função cadastro()).

             elif A.upper()=='N':
                break#Se 'n' ou 'N',sai do laço de repetição.

             else:
                 print("Digite somente S ou N ( SIM ou NÃO)")
                 continue#Volta para o laço se o valor dado for diferente de S e N ( s e n ).
             return#Foi colocado para solucionar o problema de ter que digitar a opção 'N'(não) duas vezes no input da variável A, por trazer ao usuário a pergunta do input da variável A duas vezes. Porém isso só acontece se digitar 'S' na primeira vez no input de A e ser direcionado para cadastrar novamente, o que consecutivamente faz retornar a mensagem de input de A mais uma vez para o usuário.


     repetirPergunta()#Executa a função de cima.
     break#Sai do laço de repetição.



def perguntas():# Ao selecionar a opção perguntas como uma das opções que aparece no menu abrirá esta função.
 global cursor#Traz a variável cursor do escorpo global para que possa ser utilizada na conexão com o banco de dados.

 while True:# Laço de repetição para continuar a aderir dados enquanto for preciso.
    while True:

       queimada=input('É consciente que a queimada favorece o aquecimento global?(S/N):')#Primeira pergunta da entrevista.
       #Abaixo está uma condição para que continue no laço de repetição caso não digite uma das seguintes letras:s,S,n,N.
       if queimada.upper() !='S' and queimada.upper() !='N':
            print("Digite somente S para sim ou N para nao")
            continue

       else:# Sai do laço de repetição.
            break

    while True:#Outro laço de repetição dentro de um laço de repetição. Para que retorne só nesta parte.
       derrubada = input('É consciente que a derrubada de árvores favorece o aquecimento global?(S/N):') # Segunda pergunta da entrevista.
       # Abaixo está uma condição para que continue no laço de repetição caso não digite uma das seguintes letras:s,S,n,N.
       if derrubada.upper() != 'S' and derrubada.upper() != 'N':
            print("Digite somente S para sim ou N para nao")
            continue
       else:# Sai do laço de repetição.
            break

    while True:#Outro laço de repetição dentro de um laço de repetição. Para que retorne só nesta parte.
       solo = input('É consciente que a pecuária empobrece o solo tornando a infertil podendo por seguinte favorecer o aquecimento glocal?(S/N):')  # Terceira pergunta da entrevista.
       # Abaixo está uma condição para que continue no laço de repetição caso não digite uma das seguintes letras:s,S,n,N.
       if solo.upper() != 'S' and solo.upper() != 'N':
            print("Digite somente S para sim ou N para nao")
            continue
       else:# Sai do laço de repetição.
          
            break

    #A variável comando recebe comandos do mysql para executar um insert com os valores dos inputs feitos nas perguntas anteriores( como values nas colunas pergunta1,pergunta2 e pergunta 3 respectivamentes em mysql (na tabela Perguntas)).
    comando = f"""INSERT INTO Perguntas(pergunta1,pergunta2,pergunta3) VALUES('{queimada}','{derrubada}','{solo}')"""
    cursor.execute(comando)#Executa a ação de INSERT da variável comando no banco de dados do mysql.
    conexao.commit()#Comando que possibilita editar o banco de dados, utilizado para gravar e alterar valores.



    while True:#Outro laço de repetição. Criado para que retorne somente nesta parte.
      pergunta=input('Deseja realizar mais entrevista?(S/N):')#Pergunta para decidir se continuará com a entrevista(no laço de repetição) ou se deseja sair.
      if pergunta=='S' or pergunta=='s':#Se 's' ou 'S' volta para o inicio da função perguntas().
          return perguntas()

      elif pergunta == 'N' or pergunta == 'n':#Se 'n' ou 'N' sai do laço de repetição.
          break

      else:#Se digitar algo fora do s,S,n,N volta ao imput da variável pergunta(volta no laço de repetição).
          print("Digite somente S ou N ( SIM ou NÃO)")
          continue
    break# termina o laço, sai da função perguntas voltando para o menu principal.




def argumento():# Ao selecionar a opção argumento como uma das opções que aparece no menu abrirá esta função.
    while True:#Estrutura de repetição para continuar arquivando dados e informações da etapa de conclusão.
        global cursor#Traz a variável cursor do escorpo global para que possa ser utilizada na conexão com o banco de dados.

        aceitacao=input('Concorda com todas as recomendações para evitar o aquecimento glocal?(S/N):')#Pergunta conclusiva que demonstra se o entrevistado concorda com todas as recomendações para proteger o meio ambiente ou não.

        # Abaixo está uma condição para que continue no laço de repetição caso não digite uma das seguintes letras:s,S,n,N.
        if aceitacao.upper()!='S' and aceitacao.upper()!='N':
            print("Digite somente S(para SIM) ou N(para NÃO)")
            continue
        else:
            break#Sai do laço de repetição caso tenha digitado corretamente.

    while True:#Outro laço de repetição para ser possível de retornar somente nesta parte.

       global cursor#Traz a variável cursor do escorpo global para que possa ser utilizada na conexão com o banco de dados.
       opniao=input('Alguma sugestão que queira propor ou argumento de discordância que deseja expor?(S/N):')#Pergunta se deseja arquivar uma sugestão ou argumento(conrcordância e discordância).

       if opniao.upper()=='S':#Se sim pede para digitar a sugestão ou o argumento.

           acao=input(str('Digite a sugestão ou o argumento:'))#A sugestão ou o argumento do entrevistado.

           #A variável comando1 recebe comandos de INSERT do mysql para aderir o concentimento e sugestão ou o argumento dos inputs anteriores no banco de dados( como values nas colunas aceitabilidade e argumento em mysql[na tabela Argumento]).
           comando1 = f"""INSERT INTO Argumento(aceitabilidade,argumento) VALUES('{aceitacao}','{acao}')"""
           cursor.execute(comando1)#Executa a ação de INSERT da variável comando1 no banco de dados do mysql.
           conexao.commit()#Comando que possibilita editar o banco de dados, utilizado para gravar e alterar valores.
           break  # Sai do laço.

       elif opniao.upper()=="N":#Caso responda N ou n (não) no input da variável argumento armazenará no banco de dados do mysql, somente o input da variável aceitação.

           comando2 = f"""INSERT INTO Argumento(aceitabilidade) VALUES('{aceitacao}')"""
           cursor.execute(comando2)#Executa a ação de INSERT da variável comando2 no banco de dados do mysql.
           conexao.commit()#Comando que possibilita editar o banco de dados, utilizado para gravar e alterar valores.
           break  # Sai do laço.

       else:#Volta para o laço de repetição, pois digitou opção que não é sim ou não.
           print("Digite somente S(para SIM) ou N(para NÃO)")
           continue

    while True:#Estrutura de repetição para tratar retorno às perguntas para o usuário.

       pergunta=input('Deseja arquivar mais evidências?(S/N):')#Pergunta se deseja arquivar mais evidência.
       if pergunta=='S' or pergunta=='s':

           return argumento() #Retornará para a mesma função que está caso digite s ou S( um sim).

       elif pergunta=='N' or pergunta=='n':#Sai do laço de repetição.
           break

       else:#Volta para o laço de repetição, pois digitou opção que não é sim  e nem não.
           print("Digite somente S(para SIM) ou N(para NÃO)")
           continue
    return#Retorna para o menu principal.

def consulta():# Ao selecionar a opção consulta como uma das opções que aparece no menu abrirá esta função.
    while True:#Estrutura de repetição para continuar com o laço da consulta( loop para realizar consulta várias vezes).
        global cursor#Traz a variável cursor do escorpo global para que possa ser utilizada na conexão com o banco de dados.

        option = input('Selecione o campo desejado a consultar:1-dados do cadastro/2-Perguntas/3-Argumentos/4-retornar:')#Pergunta com 4 opções selecionáveis.

        if option=='1':#Cai nessa condição ao selecionar a opção 1 na pergunta anterior. Poderá consultar os dados de cadastro.

            comando = f"""SELECT * FROM Cadastro"""#Variável comando recebe um comando na linguagem mysql para selecionar valores e colunas(todas) da tabela Cadastro.
            cursor.execute(comando)#Executa o comando de SELECT da variável comando no banco de dados do mysql.
            response=cursor.fetchall()#fechall é utilizado para consultas(trazer valores e colunas), ela inclui todas as linhas.
            print('\n')
            print(response)#Imprimi a seleção do mysql.
            print('\n')

        elif option=='2':#Cai nessa condição ao selecionar a opção 2 na pergunta anterior. Poderá consultar os dados referentes as perguntas.

            comando1_2 = f"""SELECT count(*) FROM Perguntas"""#Variável comando1_2 recebe um comando na linguagem mysql para selecionar registros(todos) da tabela Perguntas.
            cursor.execute(comando1_2)#Executa o comando de SELECT da variável comando1_2 no banco de dados do mysql.
            response2=cursor.fetchall()#fechall é utilizado para consultas(trazer valores e colunas), ela inclui todas as linhas.
            print('\n')
            print('Total de entrevistados: {} .'.format(response2))#Imprimi a seleção do mysql.
            print('\n')

            # Variável comando2 recebe um comando na linguagem mysql para selecionar registros(todos) da tabela Perguntas onde a coluna pergunta1 for s ou S(como values no mysql).
            comando2=f"""SELECT count(*) from Perguntas WHERE pergunta1='s' or pergunta1='S'"""
            cursor.execute(comando2)#Executa o comando de SELECT da variável comando2 no banco de dados do mysql.
            response3=cursor.fetchall()#fechall é utilizado para consultas(trazer valores e colunas), ela inclui todas as linhas.
            print('O número de indivíduos cientes de que a queimada causa danos ao ecossistema é de {} indivíduo(s).'.format(response3))#Imprimi a seleção do mysql.

            # Variável comando2_1 recebe um comando na linguagem mysql para selecionar registros(todos) da tabela Perguntas onde a coluna pergunta1 for n ou N(como values no mysql).
            comando2_1=f"""SELECT count(*) from Perguntas WHERE pergunta1='n' or pergunta1='N'"""
            cursor.execute(comando2_1)#Executa o comando de SELECT da variável comando2_1 no banco de dados do mysql.
            response4=cursor.fetchall()#fechall é utilizado para consultas(trazer valores e colunas), ela inclui todas as linhas.
            print('Ainda assim {} indivíduos permaneciam sem estarem cientes de que a queimada favorece o dano ecossistêmico.'.format(response4))#Imprimi a seleção do mysql.
            print('\n')

            # Variável comando3 recebe um comando na linguagem mysql para selecionar registros(todos) da tabela Perguntas onde a coluna pergunta2 for s ou S(como values no mysql).
            comando3 = f"""SELECT count(*) from Perguntas WHERE pergunta2='s' or pergunta2='S'"""
            cursor.execute(comando3)#Executa o comando de SELECT da variável comando3 no banco de dados do mysql.
            response5=cursor.fetchall()#fechall é utilizado para consultas(trazer valores e colunas), ela inclui todas as linhas.
            print('O número de indivíduos cientes de que a derrubada de árvores causa danos ao ecossistema é de {} indivíduo(s).'.format(response5))#Imprimi a seleção do mysql.

            # Variável comando3_1 recebe um comando na linguagem mysql para selecionar registros(todos) da tabela Perguntas onde a coluna pergunta2 for n ou N(como values no mysql).
            comando3_1 = f"""SELECT count(*) from Perguntas WHERE pergunta2='n' or pergunta2='N'"""
            cursor.execute(comando3_1)#Executa o comando de SELECT da variável comando3_1 no banco de dados do mysql.
            response6=cursor.fetchall()#fechall é utilizado para consultas(trazer valores e colunas), ela inclui todas as linhas.
            print('Ainda assim {} indivíduos permaneciam sem estarem cientes de que a derrubada de árvores favorece o dano ecossistêmico.'.format(response6))#Imprimi a seleção do mysql.
            print('\n')

            # Variável comando4 recebe um comando na linguagem mysql para selecionar registros(todos) da tabela Perguntas onde a coluna pergunta3 for s ou S(como values no mysql).
            comando4 = f"""SELECT count(*) from Perguntas WHERE pergunta3='s' or pergunta3='S'"""
            cursor.execute(comando4)#Executa o comando de SELECT da variável comando4 no banco de dados do mysql.
            response7=cursor.fetchall()#fechall é utilizado para consultas(trazer valores e colunas), ela inclui todas as linhas.
            print('O número de indivíduos cientes de que a pecuária causa o empobrecimento do solo podendo afetar o equilíbrio ecossistemico é de {} indivíduo(s).'.format(response7))#Imprimi a seleção do mysql.

            # Variável comando4_1 recebe um comando na linguagem mysql para selecionar registros(todos) da tabela Perguntas onde a coluna pergunta3 for n ou N(como values no mysql).
            comando4_1= f"""SELECT count(*) from Perguntas WHERE pergunta3='n' or pergunta3='N'"""
            cursor.execute(comando4_1)#Executa o comando de SELECT da variável comando4_1 no banco de dados do mysql.
            response8=cursor.fetchall()#fechall é utilizado para consultas(trazer valores e colunas), ela inclui todas as linhas.
            print('Ainda assim {} indivíduos permaneciam sem estarem cientes de que a pecuária causa o empobrecimento do solo podendo favorecer o dano ecossistêmico.'.format(response8))#Imprimi a seleção do mysql.
            print('\n')#Espaçamento.

        elif option=='3':#Cai nessa condição ao selecionar a opção 3 na pergunta anterior.
            print('\n')
            #Variável comando5 recebe comando na linguagem mysql para selecionar o número de registros da coluna aceitabilidade referente a tabela Argumento, onde os valores forem s ou S(em mysql).
            comando5= f"""SELECT count(aceitabilidade) from Argumento WHERE aceitabilidade='s' or aceitabilidade='S'"""
            cursor.execute(comando5)#Executa o comando de SELECT da variável comando5 no banco de dados do mysql.
            response9=cursor.fetchall()#fechall é utilizado para consultas(trazer valores e colunas), ela inclui todas as linhas.

            # Variável comando6 recebe comando na linguagem mysql para selecionar o número de registros da coluna aceitabilidade referente a tabela Argumento, onde os valores forem n ou N(em mysql).
            comando6 = f"""SELECT count(aceitabilidade) from Argumento WHERE aceitabilidade='n' or aceitabilidade='N'"""
            cursor.execute(comando6)#Executa o comando de SELECT da variável comando6 no banco de dados do mysql.
            response10=cursor.fetchall()#fechall é utilizado para consultas(trazer valores e colunas), ela inclui todas as linhas.

            print('Numero de individuos apoiadores: {} , numero de individuos não apoiadores: {}'.format(response9, response10))#Imprimi a seleção do mysql, referente ao comando6 e comando7.

            # Variável comando7 recebe comando na linguagem mysql para selecionar valores das colunas cod_conclusao e argumento da tabela Argumento.
            comando7= f"""SELECT cod_argumento,argumento from Argumento"""
            cursor.execute(comando7)#Executa o comando de SELECT da variável comando7 no banco de dados do mysql.
            response11=cursor.fetchall()#fechall é utilizado para consultas(trazer valores e colunas), ela inclui todas as linhas.
            print(response11)#Imprimi a seleção do mysql.
            print('\n')#Espaçamento.

        elif option=='4':#Se a opção escolhida for 4 sai do laço de repetição.
            break

        else:#Caso digite uma opção inválida volta para o laço de repetição.
            print("Opção inválida!")
            continue
def remocao():# Ao selecionar a opção remocao como uma das opções que aparece no menu abrirá esta função.
        global cursor  # Traz a variável cursor do escorpo global para que possa ser utilizada na conexão com o banco de dados.
        y=input('Escolha o campo a remover(1-cadastro e perguntas/2-argumento/3-retornar):')#Três possibilidade selecionáveis de opção nesta pergunta.

        if y=='1':#Se o valor digitado for 1 no input de cima(Y).

         w=int(input('Digite o código para o descadastramento desejado(esta ação apagará os dados referentes ao cadastro e perguntas):'))#Pergunta ao usuário o codigo referente para poder remover os dados pertencente.

         #Comando abaixo desabilita checagem da foreign key para que possa mudar os valores da primary key.
         comandof = f"""SET foreign_key_checks = 0; """
         cursor.execute(comandof)  # Executa o comando SET da variável comando1 no banco de dados do mysql.
         conexao.commit()  # Comando que possibilita editar o banco de dados, utilizado para gravar e alterar valores.

         #Variável comando1 receberá o comando DELETE do mysql para apagar valores da tabela Cadastro onde o valor da coluna  cod_cadastro for referente ao valor do input da variável w.
         comando1=f"""DELETE from Cadastro WHERE cod_cadastro={w} """
         cursor.execute(comando1)#Executa o comando DELETE da variável comando1 no banco de dados do mysql.
         conexao.commit()#Comando que possibilita editar o banco de dados, utilizado para gravar e alterar valores.

         # Variável comando1_1 receberá o comando DELETE do mysql para apagar valores da tabela Perguntas onde o valor da coluna  cod_perguntas for referente ao valor do input da variável w.
         comando1_1= f"""DELETE from Perguntas WHERE cod_perguntas={w}"""#Executa o codigo DELETE da variável comando1_1 no banco de dados do mysql.
         cursor.execute(comando1_1)  # Executa o comando DELETE da variável comando1_1 no banco de dados do mysql.
         conexao.commit()  # Comando que possibilita editar o banco de dados, utilizado para gravar e alterar valores.

         #Comando abaixo habilita novamente as checagens padrões da foreign key.
         comandof2 = f"""SET foreign_key_checks = 1; """
         cursor.execute(comandof2)  # Executa o comando SET da variável comando1 no banco de dados do mysql.
         conexao.commit()  # Comando que possibilita editar o banco de dados, utilizado para gravar e alterar valores.

         print("O cadastro e a entrevista referente ao codigo{} foram removidos com sucesso!".format(w))

        elif y=='2':#Se o valor digitado for 2 no input de cima.

         v= int(input('Digite o codigo a qual a sugestão ou o argumento pertencente será removido:'))#Pergunta ao usuário o codigo referente para poder remover os dados pertencente.

         # Comando abaixo desabilita checagem da foreign key para que possa mudar os valores da primary key.
         comandof = f"""SET foreign_key_checks = 0; """
         cursor.execute(comandof)  # Executa o comando SET da variável comando1 no banco de dados do mysql.
         conexao.commit()  # Comando que possibilita editar o banco de dados, utilizado para gravar e alterar valores.

         # Variável comando2 receberá o comando DELETE do mysql para apagar valores da tabela Argumento onde o valor da coluna  cod_argumento for referente ao valor do input da variável v.
         comando2=f"""DELETE from Argumento argumento WHERE cod_argumento={v}"""
         cursor.execute(comando2)#Executa o comando DELETE da variável comando2 no banco de dados do mysql.
         conexao.commit()#Comando que possibilita editar o banco de dados, utilizado para gravar e alterar valores.
         print("O argumento referente ao codigo {} foi removido com secesso!".format(v))

         # Comando abaixo habilita novamente as checagens padrões da foreign key.
         comandof2 = f"""SET foreign_key_checks = 1; """
         cursor.execute(comandof2)  # Executa o comando SET da variável comando1 no banco de dados do mysql.
         conexao.commit()  # Comando que possibilita editar o banco de dados, utilizado para gravar e alterar valores.


        elif y=='3':#Caso digite a opção 3 retornará para o menu.
            return

        else:#Caso digite uma opção inválida retorna para o início da mesma função executando ela mesma.
            print("Digitou uma opção inválida!")
            remocao()

def resetar ():#Função para resetar o programa. Aparecerá ao selecionar a opção 6 pelo Menu.
    print('\n')#Espaçamento.
    global cursor  # Traz a variável cursor do escorpo global para que possa ser utilizada na conexão com o banco de dados.

    while True:  # Laço de repetição.

     r=input("Você realmente deseja resetar o programa? (S/N):")#Pergunta ao usuário se deseja resetar.

     if r=="N" or r=="n":#Se a escolha for não volta para no Menu.
        return

     elif r=="S" or r=="s":#Se a escolha for sim.
      remocao=f"""DROP DATABASE extensionista2;"""#Variável remocao recebe comando de DROP em mysql. A ação irá remover o bando de dados.
      criacao0=f"""CREATE DATABASE extensionista2;"""#Variável criacao0 recebe o comando de CREATE para criar o database no mysql.
      uso=f"""USE extensionista2;"""#Variável uso irá receber o comando USE do mysql para usar o database criado.
      criacao1=f"""CREATE TABLE Perguntas( cod_perguntas int(3) auto_increment, pergunta1 char , pergunta2 char  , pergunta3 char, constraint pk_perguntas primary key(cod_perguntas) );"""#Variável criacao1 irá receber comandos para criar a tabela e as colunas(tabela Perguntas e suas colunas).
      criacao2=f"""CREATE TABLE Cadastro( cod_cadastro int(3) auto_increment, nome varchar(100) not null, endereco varchar(100) , telefone int, constraint pk_cadastro primary key(cod_cadastro));"""#Variável criacao2 irá receber comandos para criar a tabela e as colunas(tabela Cadastro e suas colunas).
      criacao3=f"""CREATE TABLE Argumento( cod_argumento int(3) auto_increment, aceitabilidade char , argumento varchar(100), constraint pk_argumento primary key(cod_argumento) );"""#Variável criacao3 irá receber comandos para criar a tabela e as colunas(tabela Argumento e suas colunas).
      #A variável de baixo, criacao4, irá criar a tabela Menu com as chaves estrengeiras referentes às demais tabelas geradas.
      criacao4=f"""CREATE TABLE Menu(cod_menu int(3) auto_increment primary key,cod_perguntas int(3),cod_cadastro int(3), cod_argumento int(3), constraint fk_perguntas foreign key(cod_perguntas) references Perguntas(cod_perguntas), constraint fk_cadastro foreign key(cod_cadastro) references Cadastro(cod_cadastro),constraint fk_argumento foreign key(cod_argumento) references Argumento(cod_argumento));"""

      #Os códigos abaixo irão executar os comandos das variáveis de cima( executar no mysql).

      cursor.execute(remocao)  # Executa o codigo DROP da variável remocao (execução é feita no banco de dados do mysql).
      conexao.commit()  # Comando que possibilita editar o banco de dados, utilizado para gravar e alterar valores.

      cursor.execute(criacao0) # Executa o codigo CREATE da variável criacao0 (execução é feita no banco de dados do mysql).
      conexao.commit()  # Comando que possibilita editar o banco de dados, utilizado para gravar e alterar valores.

      cursor.execute(uso) # Executa o codigo USE da variável uso (execução é feita no banco de dados do mysql).
      conexao.commit()  # Comando que possibilita editar o banco de dados, utilizado para gravar e alterar valores.

      cursor.execute(criacao1) # Executa o codigo CREATE da variável criacao1 (execução é feita no banco de dados do mysql).
      conexao.commit()  # Comando que possibilita editar o banco de dados, utilizado para gravar e alterar valores.

      cursor.execute(criacao2) # Executa o codigo CREATE da variável criacao2 (execução é feita no banco de dados do mysql).
      conexao.commit()  # Comando que possibilita editar o banco de dados, utilizado para gravar e alterar valores.

      cursor.execute(criacao3) # Executa o codigo CREATE da variável criacao3 (execução é feita no banco de dados do mysql).
      conexao.commit()  # Comando que possibilita editar o banco de dados, utilizado para gravar e alterar valores.

      cursor.execute(criacao4) # Executa o codigo CREATE da variável criacao4 (execução é feita no banco de dados do mysql).
      conexao.commit()  # Comando que possibilita editar o banco de dados, utilizado para gravar e alterar valores.


      print("O programa foi resetado com sucesso!")#Menssagem de bem sucedido
      break
     else:#Caso o usuário digite uma opção inválida voltará para o laço.
        print("Digite somente S para sim ou N para não.")
        continue

print('\n')
x=print('Bem vindo ao trabalho ecológico comunitário!')#Menssagem de boas vindas.
z=print('Protótipo desenvolvido por Max Alexandre Ken Iti Oda Ru:4282741')
while True:#Laço de repetição para retornar ao início caso digite a opção inválida( utilizando continue).


 print('--------------Menu Principal-------------------------------------------------------------------------------------------------------------------------------')
 print('\n')
 print('Registros de dados armazenados até o momento:')#Print que fará o usuário entender que abaixo estarão listados todas as ações gravadas no programa.

 #Abaixo foi elaborado um método para que as foreign keys herdem os valores das primary keys para mostrar na tela do menu o número de registros salvos.
 #Poderia ter usado o Update Cascade porém esse comando estava causando erro durante a remoção de valores específico e foi substituido pela inserção manual.

 #O comando abaixo deleta do banco de dados mysql, os valores de todas as foreign key presentes na Tabela Menu. Isso foi feito para solucionar o problema de iterações repetidas( de valores nas foreign keys) em todas as vezes que o Menu deste programa for acessado.
 comandoClean=f"""DELETE from Menu"""
 cursor.execute(comandoClean)# Executa o codigo da variável comandoClean(execução no banco de dados do mysql).
 conexao.commit()# Comando que possibilita editar o banco de dados, utilizado para gravar e alterar valores.

 #Os comandos abaixo copiam os valores das respectivas chaves primárias de cada tabela e aderem seus valores nas chaves estrangeiras da tabela Menu.

 comandoCadastro = f"""Insert into Menu(cod_cadastro) Select distinct cod_cadastro from Cadastro;"""
 cursor.execute(comandoCadastro)# Executa o codigo da variável comandoCadastro(execução no banco de dados do mysql).
 conexao.commit()# Comando que possibilita editar o banco de dados, utilizado para gravar e alterar valores.
 comando1 = f"""SELECT count(cod_cadastro) from Menu;"""
 cursor.execute(comando1)# Executa o codigo da variável comando1(execução no banco de dados do mysql).
 response2 = cursor.fetchall()#Irá trazer os valores da consulta da variável comando1.
 print("Número total de cadastros realizados: {}".format(response2))  # Imprimi a seleção do mysql.

 comandoPerguntas = f"""Insert into Menu(cod_perguntas) Select distinct cod_perguntas from Perguntas;"""
 cursor.execute(comandoPerguntas)# Executa o codigo da variável comandoPerguntas(execução no banco de dados do mysql).
 conexao.commit()# Comando que possibilita editar o banco de dados, utilizado para gravar e alterar valores.
 comando0 = f"""SELECT count(cod_perguntas) from Menu;"""
 cursor.execute(comando0)# Executa o codigo da variável comando0(execução no banco de dados do mysql).
 response = cursor.fetchall()#Irá trazer os valores da consulta da variável comando0.
 print("Número total de sessão de perguntas realizadas:{}".format(response))# Imprimi a seleção do mysql.

 comandoArgumento = f"""Insert into Menu(cod_argumento) Select cod_argumento from Argumento;"""
 cursor.execute(comandoArgumento)# Executa o codigo da variável comandoArgumento(execução no banco de dados do mysql).
 conexao.commit()# Comando que possibilita editar o banco de dados, utilizado para gravar e alterar valores.
 comando2 = f"""SELECT count(cod_argumento) from Menu;"""
 cursor.execute(comando2)# Executa o codigo da variável comando2(execução no banco de dados do mysql).
 response3 = cursor.fetchall()#Irá trazer os valores da consulta da variável comando2.
 print("Número total de argumentos coletados: {}".format(response3))  # Imprimi a seleção do mysql.
 print('\n')#Espaçamento.

 #Listará as opções que o usuário poderá realizar no programa.
 y=input('Selecione a ação desejada:1 para cadastro/ 2 para perguntas/ 3 para coleta de argumentos/ 4 para consulta/5 para descadastrar ou remover/6 para resetar o programa/7 para sair:')#Pergunta com 7 opções disponíveis.
 if y=='1':#Leva a execução da função cadastro().Serve para cadastrar o nome, endereço e telefone.
     cadastro()
 elif y=='2':#Leva a execução da função entrevista().Serve para arquivar indícios de conhecimento.
     perguntas()
 elif y=='3':#Leva a execução da função conclusao().Serve para arquivar argumentos e a conclusão realizada da entrevista.
     argumento()
 elif y=='4':#Leva a execução da função consulta().Serve para consultar os dados armazenados dos cadastros,entrevistas,argumentos e conclusões finais.
     consulta()
 elif y=='5':#Leva a execução da função remocao().Serve para remover dados de cadastros e argumentos.
     remocao()
 elif y=='6':#Leva a execução da função resetar(). Serve para resetar todos os dados armazenados.
     resetar()
 elif y=='7':#Sai do laço de repetição e encerrar o programa.
     break
 else:
     print("Opção inválida!")# Se digitar opção inexistente volta para o laço de repetição.
     continue

