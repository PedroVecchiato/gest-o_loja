Sistema de Gestão Básico em Python

Sistema simples para gerenciar vendas, cadastro de clientes, controle de estoque e geração de relatórios, utilizando arquivos JSON para persistência de dados.

-----------------------------------------------------------------------

Funcionalidades

- Realizar vendas com controle automático do estoque
- Cadastro de clientes com validação (Básica) de dados (nome, CPF e telefone)
- Cadastro e reestoque de produtos no estoque
- Listagem de produtos e clientes cadastrados
- Geração e restauração de relatórios de vendas
- Interface simples de menu via terminal

-----------------------------------------------------------------------

Como usar

1. Clone o repositório (Dentro do Terminal): 

    git clone  https://github.com/PedroVecchiato/gest-o_loja.git
    cd https://github.com/PedroVecchiato/gest-o_loja.git

2. Execute o programa principal (Dentro do Terminal):

    python main.py

3. Use o menu para navegar pelas opções:
   1: Realizar Venda
   2: Cadastrar Cliente
   3: Cadastrar Produto
   4: Reestocar Produto
   5: Listar Produtos
   6: Listar Clientes
   7: Gerar Relatório de Vendas
   8: Restaurar Vendas do Relatório
   9: Sair

-----------------------------------------------------------------------

Estrutura dos Arquivos

- main.py: Gerencia o fluxo do programa e integra módulos
- carregamento_dados.py: Funções para carregar e salvar dados JSON
- clientes.py: Cadastro e listagem de clientes com validação
- estoque.py: Cadastro, reestoque e listagem de produtos
- vendas.py: Realização de vendas, listagem, geração e restauração de relatórios
- utilidades.py: Funções auxiliares para exibição de menus e textos

-----------------------------------------------------------------------

Dados persistidos

Os dados são salvos em arquivos JSON locais:

- clientes.json: dados dos clientes cadastrados
- estoque.json: produtos e quantidades em estoque
- vendas.json: registros das vendas realizadas
- relatorio.txt: relatório formatado das vendas

-----------------------------------------------------------------------

Requisitos

- Python 3.x instalado

-----------------------------------------------------------------------

* Os arquivos JSON e RELATORIO.TXT Ficaram normalmente no seguinte caminho: C:\Users\seu_usuario\gest-o_loja
