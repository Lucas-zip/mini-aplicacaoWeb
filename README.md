# Projeto 02 - Mini-projeto Web utilizando Docker + PostgreSQL

## Documentação para a instalação e configuração necessárias para a execução do mini-projeto Web.

#### Membros da Equipe: 

Lucas Gabriel Simões Marinho - 06009936
<br>
Julia Scarpi Campos - 06006846
<br>
Luna Ferreira de Mattos - 0600983
<!-- OBJETIVO OBRIGATÓRIO: TERMINAR DE PREENCHER ESTA DOCUMENTAÇÃO -->

### Sobre o projeto 

Este projeto é uma aplicação web simples que permite a execução de comandos SQL em um banco de dados PostgreSQL. Ele utiliza Flask para o backend e HTML/CSS para o frontend. O projeto está configurado para ser executado em contêineres Docker, facilitando a configuração e a execução em diferentes ambientes.

### Pré-instalação (Ubuntu - objetivo de avaliação optativo)

0. Primeiramente, vale ressaltar que esse projeto utiliza o framework Flask, escrito em Python, para o back-end da aplicação. O motivo da escolha dessa ferramenta são dois: (i) curva de aprendizado mais rápida e (ii) utiliza Python, que será a linguagem de programação vista no próximo semestre.

1. Antes de tudo, verifique se o Docker está instalado no Ubuntu. Para isso, abra o terminal pelo atalho Ctrl + Alt + T e digite o seguinte comando:

bash
docker --version

Caso apareça uma mensagem semelhante a Docker version 26.1.4, build 5650f9b, o Docker está instalado. Caso contrário, é preciso seguir o tutorial de instalação Docker presente [aqui](https://drive.google.com/file/d/1kgtSUo5lSGNbZ4mQMIsRnIepf6Haiy91/view?usp=sharing).

2. Em seguida, remova todos os contâineres do PostgreSQL e pgAdmin que podem estar presentes desde a última demonstração. Para isso, execute o seguinte comando:

bash
docker rm -f $(docker ps -a -q)

Caso algum container tenha sido removido, parte de sua numeração hash aparecerá na tela. Execute o comando docker ps -a para mostrar todos os contâineres, inclusive os desabilitados. Se nada aparecer, então pule para o Passo 3.

3. Ceritifque-se de estar dentro do diretório Projeto2 para executar o próximo comando:

bash
docker-compose up --build -d

Este comando executará o arquivo docker-compose.yml presente no diretório Projeto2, que orquestrará o download das imagens do PostgreSQL e pgAdmim, como também a criação dos contâineres. Após o término do comando, execute docker ps e verifique se todos os côntaineres estão rodando. Neste caso, ainda não estarão porque vocês ainda não configuraram a conexão com o banco de dados no arquivo app.py. Para ver mais informações sobre o erro, execute o comando docker logs projeto2_web_1, sendo projeto2_web_1 o nome do container. Verifique o nome do seu container da aplicação Web a partir do comando docker ps -a.

Daqui em diante, o projeto está pré-instalado. Para instalá-lo completamente, será preciso atender aos objetivos de avaliação obrigatórios listados no enunciado do trabalho. Importante: após a finalização do projeto, rode novamente o comando docker-compose up --build -d para levantar o container do aplicativo Web. Após configurar o caminho do banco em app.py, você precise remover os contâineres com o comando docker rm -f $(docker ps -a -q), rode o comando docker-compose up --build -d duas vezes para que o container do aplicativo seja devidamente levantado. Para isso, verifique a partir do comando docker ps se há três contâineres.

### Pré-instalação (Windows)

Utilize o tutorial disponivel em [https://youtu.be/L_2l8XTCPAE] para instalar o PostgreSQL e verificar onde fica o Query Tool para a execução de comandos. Caso crie o banco de dados PDV conforme mostrado no vídeo, dispense o script init.sql.

### Como a Aplicação Funciona
#### Arquivo app.py
Este é o coração da aplicação. Ele realiza as seguintes funções:

- Conexão com o Banco de Dados:

A função connect_to_db() tenta conectar ao banco de dados PostgreSQL, utilizando os parâmetros fornecidos (dbname, user, password, host, port). Em caso de falha na conexão, ele espera 5 segundos e tenta novamente.
A conexão é criada uma vez e reutilizada durante a execução da aplicação.

- Rota Principal:

A rota '/' aceita tanto requisições GET quanto POST.
No método GET, simplesmente renderiza o template HTML.
No método POST, recebe um comando SQL do formulário, executa-o no banco de dados e captura os resultados ou erros.

- Execução de Comandos SQL:

O comando SQL inserido pelo usuário é executado usando um cursor.
Se a execução for bem-sucedida, os resultados são capturados e exibidos na página.
Se ocorrer um erro durante a execução do comando SQL, o erro é tratado, uma mensagem de erro é exibida e a transação é revertida (rollback).

#### Arquivo index.html
Este é o template HTML que define a interface do usuário. Ele realiza as seguintes funções:

- Formulário de Entrada:

O formulário permite que o usuário insira comandos SQL.
Quando o formulário é enviado, um POST request é feito para o servidor.

- Exibição dos Resultados:

Se houver resultados de uma consulta SQL, eles são exibidos em uma tabela.
A tabela é dinamicamente preenchida com os nomes das colunas e os dados das linhas utilizando a sintaxe Jinja2 do Flask.

- Exibição de Erros:

Se houver um erro ao executar o comando SQL, uma mensagem de erro é exibida.

### Como Executar o Projeto

- Pré-requisitos:

Docker e Docker Compose instalados(podem facilmente ser instalados com o auxílio do chatGPT).
Um banco de dados PostgreSQL configurado.

- Passos para Executar:

Clone este repositório.
Navegue até o diretório do projeto.
Configure os parâmetros do banco de dados no arquivo app.py.
Execute "docker-compose up --build -d" para iniciar a aplicação e o banco de dados.
Caso de algum problema com o comando anterior, rode "docker-compose down" e em seguida o compose up novamente.


- Acessando a Aplicação:

Abra um navegador web e navegue para http://localhost:5000.
Insira comandos SQL no formulário e veja os resultados ou erros na mesma página.

- Acessando o Banco de Dados:

Execute "docker-compose up --build -d" no terminal.
Acesse http://localhost:80.
Faça login usando "admin@pgadmin.com" e usando a senha "123456".
Crie um novo servidor. 
Em seguida siga essas instruções:

      POSTGRES_HOST: db
      POSTGRES_PORT: 5432
      POSTGRES_DB: pdv
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: 123456
<!-- OBJETIVO OBRIGATÓRIO: TERMINAR DE PREENCHER ESTA DOCUMENTAÇÃO -->
