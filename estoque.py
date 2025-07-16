from time import sleep

# ESCOLHA 3 CADASTRAR PRODUTO

def cadastrar_produto(informacao,dados):
    informacao["ID"] = len(dados)+1
    informacao["NOME"] = input('Digite o nome do produto: ')
    while True:
        try:
            informacao["PRECO"] = float(input("Digite o preço do produto: "))
                
        except ValueError:
            print('Favor digitar somente Números !')
            sleep(1.5)
            continue
        else:
            break
        
    while True:
        try:
            informacao["QTD"] = int(input('Digite a quantidade do produto: '))

        except ValueError:
            print('Favor digitar somente Números !')
            sleep(1.5)
            continue
        else:
            break

    print(f'Produto Cadastrado com Sucesso !')
    sleep(1.5)


# ESCOLHA 4 REESTOCAR PRODUTO

def reestocar_produto (dados):
    while True:
        try:
            id_produto = int(input('Digite o ID do produto a ser reestocado? '))-1

        except ValueError:
            print('Favor digitar somente Números !')
            sleep(1.5)
            continue
        else:
            break

    while True:
        try:
            quantidade = int(input('Quantidade produtos: '))
        except ValueError:
            print('Favor digitar somente Números !')
            sleep(1.5)
            continue
        else:
            break
        
    produto_escolhido = dados[id_produto]
    produto_escolhido ["QTD"] += quantidade
    print(f'Produto Reestocado com Sucesso !')
    sleep(1.5)


# ESCOLHA 5 LISTAR PRODUTOS

def listar_produtos (informacao,dados):
    print(f'{'='*85}\n\n{'ID':^8}{'NOME':^53}{'PREÇO':^13}{'QTD':^8}\n')
    for produtos in dados:
        print(f'{produtos["ID"]:^8}'
            f'{produtos["NOME"][:35]:^53}'
            f'{produtos["PRECO"]:^13.2f}'
            f'{produtos["QTD"]:^8}')
        sleep(0.15)
    print('')
    sleep(1.5)