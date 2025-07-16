from time import sleep

def linha():
    print(f'{'=-'*31}')

def letra_devagar_centralizado(texto,interavalo,largura=85,quebra_linha=True):
    texto = texto.center(largura)
    for letra in texto:
        print(letra,end='',flush=True)
        sleep(interavalo)
    if quebra_linha == True:
        print()

def letra_devagar(texto,intervalo):
    for letra in texto:
        print(letra, end = '',flush = True)
        sleep(intervalo)
        



def menu_cabeçario ():
        for c in range (85):
            print(f'{'='}',end='',flush=True) # Linha de cima com delay de 0.030 sec
            sleep(0.015)
        print(end=""'\n')

        (letra_devagar_centralizado('MENU DE GERENCIAMENTO',0.015,85,False))
        print(end=""'\n')

        for c in range (85):
            print(f'{'='}',end='',flush=True) # Linha de baixo com delay de 0.030 sec
            sleep(0.015)
        print()


def menu_opcoes ():
    print('\n[1] Realizar Venda')
    sleep(0.15)
    print('[2] Cadastrar Cliente')
    sleep(0.15)
    print('[3] Cadastrar Produto')
    sleep(0.15)
    print('[4] Reestocar Produto')
    sleep(0.15)
    print('[5] Listar Produtos')
    sleep(0.15)
    print('[6] Listar Clientes')
    sleep(0.15)
    print('[7] Relatório Vendas')
    sleep(0.15)
    print('[8] Restaurar Vendas')
    sleep(0.15)
    print('[9] Sair')
    sleep(0.15)
    
print('')
