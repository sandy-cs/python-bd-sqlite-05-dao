# python-bd-sqlite-05-dao

### SQLite Viewer

No Codespace, instalar a extensão (plugin) VS Code `SQLite Viewer`: 

![Alt: extensão (plugin) SQLite Viewer.](SQLiteViewerForVSCode.png)

# Python + SQLite: exemplo de Data Access Object (DAO)

Este projeto demonstra o padrão Data Access Object (DAO) em Python com SQLite. 

O exemplo apresenta as operações CREATE, READ, UPDATE, DELETE (CRUD): criar a tabela, cadastrar, consultar, atualizar e remover um usuário.

## Configurar o banco de dados

O projeto lê o caminho do banco pela variável `SQLITE_DB_PATH`, definida no arquivo
`.env`. 

Por exemplo:

```env
SQLITE_DB_PATH=./src/exemplo2/database/banco_de_dados.db
```

Caminhos relativos são interpretados a partir do diretório em que o programa é
executado. Se a variável não estiver definida, o programa usa:

```text
./src/exemplo2/database/teste.db
```

## Requisitos

- Python 3.8 ou superior
- Dependência para carregar variáveis do arquivo `.env`:

```bash
pip install -r requirements.txt
```

**OBS**: a __flag__ `-r` é a opção de `requirements file`: diz ao `pip` para ler de um arquivo a lista de pacotes que deve instalar. Assim, `pip install -r requirements.txt` instala as dependências listadas em `requirements.txt`. Sem `-r`, o `pip` interpretaria `requirements.txt` como se fosse o nome de um pacote a ser instalado.

O acesso ao SQLite usa a biblioteca padrão do Python (`sqlite3`).

## Executar

Na raiz do repositório, rode:

```bash
python -m src.exemplo2.main
```

**OBS**: a opção `-m` faz o `Python` executar um módulo pelo nome, usando o sistema de importação, em vez de executar um arquivo indicado por caminho. Em `python -m src.exemplo2.main`, o `Python` procura o módulo `src.exemplo2.main` e o executa como programa. Os pontos representam a hierarquia de pacotes e módulos. Normalmente, o comando é executado a partir da pasta que contém `src`. Isso difere de `python src/exemplo2/main.py`, que executa o arquivo diretamente. Usar `-m` ajuda o `Python` a reconhecer o contexto dos pacotes e pode ser importante para que `imports` relativos funcionem corretamente.

O programa cria o arquivo de banco indicado por `SQLITE_DB_PATH` (ou `teste.db`
quando a variável não estiver definida), cria a tabela `usuario` e executa o fluxo
de cadastro, consulta, atualização e remoção de usuários.

# Exercício

Em Python com SQLite, escreva um algoritmo que:

1. Cadastre veículos no banco de dados SQLite, segundo o padrão "Data Access Object" (DAO). O algoritmo deve permitir que o usuário cadastre quantos veículos forem necessários. A classe Veiculo deve possuir as propriedades: marca, modelo, número do chassi, placa e cor. Após cadastrar todos os veículos, o algoritmo deve permitir:
  - Consultar os veículos cadastrados.
  - Atualizar os veículos cadastrados.
  - Excluir os veículos cadastrados.

2. Implemente o CRUD (Create, Read, Update, Delete) do banco de dados de uma padaria, empregando o padrão "Data Access Object" (DAO). Considere as tabelas:
  - Cliente(id_cliente, nome),
  - Pedido(id_pedido, id_cliente, data_pedido, total),
  - Produto(id_produto, nome, preco) e
  - ItemPedido(id_pedido, id_produto, quantidade).


3. Implemente o CRUD (Create, Read, Update, Delete) do banco de dados de uma agência de viagens, empregando o padrão "Data Access Object" (DAO). Considere as tabelas:
  - Cliente(id_cliente, nome),
  - Reserva(id_reserva, id_cliente, id_destino, data_viagem, valor) e
  - Destino(id_destino, nome_destino, pais).

4. Implemente o CRUD (Create, Read, Update, Delete) do banco de dados de uma clínica médica, empregando o padrão "Data Access Object" (DAO). Considere as tabelas:
  - Paciente(id_paciente, nome),
  - Medico(id_medico, nome, especialidade) e
  - Consulta(id_consulta, id_paciente, id_medico, data_consulta, valor).

5. Implemente o CRUD (Create, Read, Update, Delete) do banco de dados de uma farmácia, empregando o padrão "Data Access Object" (DAO). Considere as tabelas:
  - Medicamento(id_medicamento, nome, preco),
  - Fornecedor(id_fornecedor, nome, cidade) e
  - Compra(id_compra, id_medicamento, id_fornecedor, quantidade, data_compra).

6. Refatore o exemplo desta prática, alterando a classe `ConnectionFactory`. Cada método da classe deve dar origem a uma classe em arquivo separado responsável pela funcionalidade específica do CRUD. Discuta as vantagens e desvantens dessa refatoração. A qual padrão de projeto `Gof` esta refatoração corresponde?