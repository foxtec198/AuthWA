# AuthWA
![create by icons8](assets/robot.png){width='100' .center}

## Banco de Dados Permitidos!
![MicrosoftSQLServer](https://img.shields.io/badge/Microsoft%20SQL%20Server-CC2927?style=for-the-badge&logo=microsoft%20sql%20server&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white)

## Instalação

### Como instalar
Rode o comando abaixo em seu terminal ou CMD!

    pip install authwa

### Execução

Importe o modulo e adicione a uma variavel, chamando a classe desejada!

    import authWA

    whats = authWA.WA()

    whats.enviar_msg()

## Preparando o ambiente de envio

Após criar abra o terminal(PowerShell) ou CMD.

> No windows: 
>> apertando __WIN + R__ e digitando __CMD__ pressione *Enter*

> No Linux: 
>> apertando __CTRL + T__ ou __CTRL + ALT + T__ ou __COMMAND//WIN__ e digite *TERMINAL*

Terminal

![Terminal](image-4.png)

Agora abra o WhatsApp faça o seguinte atalho *ALT + TAB*,
Para voltar ao terminal !

Para que seu codigo funcione é importante que deixe o whatsapp aberto, pois o codigo irá usar o atalho *Alt + Tab* para acessa-lo. 

![alt text](image.png)

É importante também que __não movimente ou clique com o mouse e nem pressione nenhuma tecla__ durante o processo, o indicado é ter uma maquina como servidor para que o codigo tenha mais eficiencia, mas não é obrigatório.

## Whatsapp
Envio de mensagens simples e com Imagens no o Whatsapp, para deixar sua imaginação fluir e construir suas automações!

>### Objetivo
> A Intenção deste modulo do AuthWA, é que você consiga usar a critividade para criar suas automações.

### **Envio simples de mensagem**

Para envio de mensagens simples, usando o modulo __WA__, é bem fácil, porém lembre-se bem deste módulo, pois ele será muito importante nos módulos a frente!

Importando o WA()

    from authWA import WA

    whats = WA()

A partir dai podemos utilizar seus modulos

> Dentro do WA() temos os seguintes modulos

> - enviar_msg( )
> - sql_connection( )
> - criar_imagem_SQL( )

### enviar_msg()
Está função faz um envio __simples ou com uma imagem__ embutida, para isto precisa ter preparado o ambiente.

> **Parametros**

> Nome = Nome do Contato a ser enviado a mensagem

> Mensagem = Mensagem a ser enviada ou a Legenda que vai na imagem

> Img = Aqui você devera colocar o caminho da Imagem a ser enviada

    from authWA import WA

    whats = WA()


    # Envio sem imagem
    whats.enviar_msg(
        nome = "Nome do contato",
        mensagem = "Isto foi enviado pelo AuthWA"
    )

    # Envio com imagem
    whats.enviar_msg(
        nome = "Nome do contato",
        mensagem = "Isto foi enviado pelo AuthWA"
        img = "imagens/image.png"
    )

### sql_connection()
Para realizar uma conexão com o banco de dados, precisamos de alguns parametros, lembre-se sempre que for realizar uma conexão com o banco de dados, faze-la no **incio** do projeto!
> **Parametros**
>> **Obrigatórios**

> uid = Usuário DB

> pwd = Senha de Acesso do DB

> server = Servidor do DB

>> **Opcional caso for utilizar o SQL Server**

> database = Banco de Dados a ser utilizado

> driver = Qual driver usar você encontra no site do SQL Alchemy:

> <a href = 'https://docs.sqlalchemy.org/en/20/core/engines.html'> Drivers do SQLAlchemy</a>

SQLite

![SQLITE](image-1.png)

SQL Server

![SQL SERVER](image-2.png)

MySQL

![MYSQL](image-3.png)

Exemplo de código

    from authWA import WA

    whats = WA()

    # Obrigatorio
    conn = whats.sql_connection(
        uid = "usuario.aqui",
        pwd = "suasenhavemaqui",
        server = "10.0.1.0",
    )

    # Opcionais
    conn = whats.sql_connection(
        uid = "usuario.aqui",
        pwd = "suasenhavemaqui",
        server = "10.0.1.0",
        database = "DATABASE",
        driver = "SQL Server"
    )   

    print(conn)

    # Saida do código
    // "Conexão realizada com sucesso!" 
    ou
    // "Conexão Invalida"

### criar_imagem_SQL()
Com a conexão realizada você pode agora fazer pesquisas e elas seram tranformadas em um arquivo PNG

> Parametros

> - consulta = Consulta SQL para gerar o Dataframe.

> - arquivo = Diretorio onde salvar o arquivo, este item é OPCIONAL, ja que o diretório padrão é __*dist/temp.png*__ e indicamos utilizar ele.

    from authWA import WA

    whats = WA()

    # Se conectando ao DB
    whats.sql_connection(
        uid = 'usuario.db',
        pwd = 'minhasenha',
        server = '10.10.0.10'
    )

    # Criando Imagem
    img = whats.criar_imagem_SQL(
        consulta = """
        SELECT Nome, TerminoReal as Data
        FROM Table
        """,
        arquivo = './img.png' # Lembrando que passar o arquivo é OPCIONAL
    )

    print(img)

Detalhe: A saida do print acima não será a imagem de fato e sim o caminho até ela, exemplo: __caminho/arquivo.png__

**Saida:** 

*./img.png*

**Imagem:**

![DataFrame](img.png)

## Parcial
### O que é Parcial ???
*Parcial é basicamente algo mais intenso do que uma simples mensagem !*

Sabe aquele acompanhamento que você quer fazer seja pra sua empresa ou pra uso pessoal? Aquele acompanhamento Hora a Hora, pois é com o Parcial você consegue facilmente.

Sabe Aquela mensagem te lembrando de fazer algo ou de uma agenda que você não pode esquecer e tem que receber essa mensagem numa hora especifica, com o Parcial é mais facil.

Aquela mensagem para seus clientes que lembrando das promoções, sempre em um horario especifico, com o Parcial, você consegue facilmente.

### Parcial - Hora a Hora
Bom, para criarmos o hora a hora, é bem simples, vamos usar alguns conceitos do WA() então é importante que tenha dominio com este modulo

    from authWA import Parcial

    # Para mensagens simples
    p = Parcial('','','')

    # Para mensagens com DB
    p = Parcial(
        'usuario.db',
        'minhasenha',
        '10.0.0.1' # Exemplo de Servidor
    )

    # Normalmente você quer usar o Parcial quando se trata de muitos contatos!
    # Pensando nisso, vamos utilizar um lista para os contatos 
    # Lembrano que ira enviar somente dias da Semana ou seja de Segunda a Sexta
    # Para fim de semanas e horarios exatos, iremos falar depois!

    lista_de_contatos = []

Dentro desta lista, vamos passar funções, mas para que ela não seja chamada, iremos usar uma função do Python chamada **lambda:**

<a href = "https://www.hashtagtreinamentos.com/funcoes-lambda-python?gad_source=1&gclid=CjwKCAiA_aGuBhACEiwAly57MceSncFkfqjcgHiMp7jKizAKtmOr_FXWju7Ldqj7osean_5glMJXwhoCLoYQAvD_BwE"> Clique aqui para mais informações sobre o lambda </a>

    from authWA import Parcial

    p = Parcial('','','')

    lista_de_contatos = [
        # Agora iremos criar a lambda!
        lambda: function()
    ]
No lugar desta **function()** iremos usar o nosso conhecimento do módulo WA(), iremos chamar a função de mensagem deste modulo dentro da *lambda*

Mas não precisamos importar o modulo WA() pois ele ja esta embutido no Parcial(), ele esta definido como *whats*, sendo assim podemos chama-lo usando a variavel onde colocamos o Parcial().

    from authWA import Parcial

    p = Parcial('','','')

    lista_de_contatos = [
        lambda: p.whats.enviar_mensagem(
            nome = "Contato 1",
            mensagem = "Codando com AuthWA!"
        ),
        lambda: p.whats.enviar_mensagem(
            nome = "Contato 2",
            mensagem = "Codando com AuthWA!"
        ),
        lambda: p.whats.enviar_mensagem(
            nome = "Contato 3",
            mensagem = "Codando com AuthWA!"
        ),
    ]

Certo, mas só fizemos a lista, ele ainda não vai executar de forma automática !

Para isso iremos entender outras coisinhas antes:

> Como definir horario de Inicio e horario de Fim

>> Para isso dentro do proprio Parcial() passamos estes parametros

>> Lembrando que o valor padrão dele é o horario comercial, ou seja das 08hrs as 18hrs

>> hora_inicio = 8

>> hora_final = 18

>>      from authWA import Parcial

>>      p = Parcial('','','', hora_inicio = 8, hora_final = 18)

Caso você iniciou a Parcial depois do horario de inicio, automaticamente ele vai iniciar 1 hora depois(Em ponto), por exemplo se você iniciar o codigo as 11:25 ele vai iniciar a parcial 12:00.

Caso tenha sido ao contrario, inciado antes ou iniciado depois da hora final, ele só ira iniciar no horario definido para inicio.

Exemplos: 

 Inicar o codigo as 06 com o inicio previsto as 8
