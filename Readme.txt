GERAL SOBRE A APLICAÇÃO:
Este software apresenta um aplicativo para controle financeiro, voltado primordialmente a pessoas físicas, mas podendo ser utilizado por micro empresas. 
Com esta aplicação, o usuário consegue manter o controle de suas contas bancárias, bem como gerenciar suas entradas e saídas de dinheiro. Sendo a interatividade do usuário com o programa via teclado. 

LINGUAGEM DE PROGRAMAÇÃO:
O código está escrito em linguagem Python 3, e a escrita para acessar o B.D. foi realizada em SQL.

RODAR O CÓDIGO:
Pré-requisitos para poder rodar essa aplicação:
Bancos de dados SQL com o nome “PubFuture”. Foi utilizado para testes o app “Microsort SQL Server Management Studio”;
Python 3 instalado em seu computor;
Instalar as bibliotecas Python: pyobdc, pandas, datetime;
Alterar a linha nº 15 onde está escrito  “LAPTOP-B00KFP26” para o nome do computador que está rodando essa aplicação.

Se rodar a aplicação mais de uma vez, comentar a linha 632, pois a mesma tem a função de criar as tabelas no B.D. e não é necessário criar mais de uma vez. 

GERAL SOBRE O CÓDIGO:
De forma simplificada o código segue a seguinte lógica:
Importar as biblioteca necessárias;
Criar conexão com o banco de dados;
Criar as tabelas necessárias;
Trazer a data atual;
Fazer uma varredura no na tabela “contas” do B.D. para saber se a necessidade de atualizar alguma receita ou despesa que havia sido adicionada com data futura a atual no momento do cadastro. E se houver necessidade de atualizar o saldo, o código irá varrer as receitas e as despesas para saber qual dado a ser atualizado e então atualizar, desde que já alcançado o dia para atualizar o saldo. Após a atualização, irá retirar os flags de saldo futuros se não existir outras receitas/despesas futuras..
Feitas análises iniciais, o código começa a interação com usuário através de funções, onde via teclado o usuário irá definindo o que ele deseja fazer.
