from time import sleep
import utilidades

def cadastrar_cliente (informacoes,dados):
    informacoes["ID"] = len(dados)+1
    while True:
        informacoes["NOME"] = (input('Digite o Nome do Clinte: '))
        if any(char.isdigit() for char in informacoes["NOME"]):
            print("Nome, Inválido Favor digitar somente Letras !")
            sleep(1.5)
            continue
        else:
            break
    while True:
        try:
            informacoes["CPF"] = int(input('Digite o CPF do Cliente: '))
            cpf_string=str(informacoes["CPF"])
            if len(cpf_string)!=11:
                print('CPF Inválido, Favor digitar um CPF existente !')
                sleep(1.5)
                continue
        except ValueError:
            print('Favor digitar somente Números !')
            sleep(1.5)
        else:
            break
    informacoes["NUMERO"] = int(input('Digite o Numero de Contato: '))
    while True:
        try:
            numero_cliente = str(informacoes["NUMERO"])
            if len(numero_cliente)!=11:
                print('Número Inválido, Favor digitar um Número existente !')
                sleep(1.5)
                continue
        except ValueError:
            print('Favor digitar somente Números !')
            sleep(1.5)
        else:
            break
    print('Cliente Cadastrado com Sucesso !')
    sleep(1.5)

def listar_cliente (informacoes,dados):
    print(f'{'='*85}\n\n{'ID'}{'NOME':^53}{'CPF':^15}{'TELEFONE':^14}\n')
    for clientes_cadastrados in dados:
        print(f'{clientes_cadastrados["ID"]} {clientes_cadastrados["NOME"][:35]:^53} {clientes_cadastrados["CPF"]:^13} {clientes_cadastrados["NUMERO"]:^14}')
    print('')
    sleep(1.5)