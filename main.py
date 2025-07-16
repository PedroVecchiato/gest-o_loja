from time import sleep
import carregamento_dados
import json
import utilidades
import estoque
import clientes
import vendas
# ARQUIVOS 

CLIENTES = "clientes.json"
ESTOQUE = 'estoque.json'
VENDAS = 'vendas.json'
RELATORIO = 'relatorio.txt'

# LISTAS

dados_clientes = []
dados_estoque = []
dados_vendas = []
nota_fiscal = []

# CARREGA O BANCO DE DADOS

dados_vendas = carregamento_dados.carregar_dados(VENDAS)
dados_estoque = carregamento_dados.carregar_dados(ESTOQUE)
dados_clientes = carregamento_dados.carregar_dados(CLIENTES)



# CODIGO PRINCIPAL

utilidades.menu_cabeçario()

while True:
    
    # DICIONARIOS

    informacoes_clientes = {}
    informacoes_estoque = {}
    informacoes_vendas =  {}

    while True: # Menu/Escolha
        

        utilidades.menu_opcoes()
        escolha = (input(f'\n{'Escolha uma opção: '}'))
    
        if escolha in ('1','2','3','4','5','6','7','8','9',):
            break
        else:
            print('Escolha inválida porfavor escolher um valor entre 1 e 9 !')
            sleep(0.8)
            continue

    if escolha == '1':

        vendas.realizar_venda(informacoes_vendas,dados_estoque,dados_vendas,nota_fiscal)
        carregamento_dados.salvar_dados(dados_estoque,ESTOQUE)
        vendas.listar_venda(informacoes_vendas,nota_fiscal)
        carregamento_dados.salvar_dados(dados_vendas,VENDAS)

    if escolha == '2':

        utilidades.letra_devagar_centralizado(f'\n{'=-'*15} {'Cadastro Iniciado'} {'-='*15}\n\n',0.015)
        clientes.cadastrar_cliente(informacoes_clientes,dados_clientes)
        dados_clientes.append(informacoes_clientes)
        carregamento_dados.salvar_dados(dados_clientes,CLIENTES)
        utilidades.letra_devagar_centralizado(f'\n{'-='*15} {'Cadastro Finalizado'} {'-='*15}\n',0.015)

    if escolha == '3':

        utilidades.letra_devagar_centralizado(f'\n{'=-'*15} {'Cadastro Iniciado'} {'-='*15}\n\n',0.015)
        estoque.cadastrar_produto(informacoes_estoque,dados_estoque)
        utilidades.letra_devagar_centralizado(f'\n{'-='*15} {'Cadastro Finalizado'} {'-='*15}\n',0.015)


        dados_estoque.append(informacoes_estoque.copy())
        with open(ESTOQUE, "w", encoding="utf-8") as f:  # SALVA AS INFORMAÇÕES DA LISTA INFORMACOES ESTOQUE
            json.dump(dados_estoque, f, ensure_ascii=False, indent=2)

        continue

    if escolha == '4':

        estoque.reestocar_produto(dados_estoque)
        carregamento_dados.salvar_dados(dados_estoque,ESTOQUE)

    if escolha == '5':
        utilidades.letra_devagar_centralizado(f'\n{'=-'*16} {'Produtos do Estoque'} {'-='*16}\n\n',0.015)
        estoque.listar_produtos(informacoes_estoque,dados_estoque)
        print('')
        continue

    if escolha == '6':
        utilidades.letra_devagar_centralizado(f'\n{'='}{'-='*16} {'Lista de Clientes'} {'=-'*16}{'='}\n\n',0.015)
        clientes.listar_cliente(informacoes_clientes,dados_clientes)

    if escolha == '7':

         vendas.gerar_relatorio(informacoes_vendas,dados_vendas,RELATORIO)

    if escolha == "8":
        vendas.restaurar_relatorio(informacoes_vendas,dados_vendas,VENDAS)
        carregamento_dados.salvar_dados(dados_vendas,VENDAS)

    if escolha == '9':
        utilidades.letra_devagar('Finalizando',0.2)
        utilidades.letra_devagar('.....',0.6)
        break
