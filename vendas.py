import time

def realizar_venda (informacoes_vendas,dados_estoque,dados_venda,nota_fiscal):
    agora = time.localtime()
    while True:

        while True:
            try:
                id_produto = int(input('Digite o ID do Produto: '))-1  # TRATAMENTO DE ERRO
                if id_produto>len(dados_estoque):
                    raise IndexError
            except (ValueError, IndexError):   
                print(f'ID Inváldio !, Favor digitar um ID entre 1 e {len(dados_estoque)}')
                time.sleep(1.5)
            else:
                break

        produto_escolhido = dados_estoque[id_produto]

        while True:
            try:
                informacoes_vendas["QTD"] = int(input('Digite a Quantidade do Produto: '))  # TR1ATAMENTO DE ERROS
                if produto_escolhido["QTD"]<informacoes_vendas["QTD"] or informacoes_vendas["QTD"]<=0:
                    print(f'Quantidade Indisponivel !, Quantidade em Estoque: {produto_escolhido["QTD"]}')
                    time.sleep(1.5)
                    continue
            except:
                print('Quantidade Inválida, Favor Digitar somente numeros !')
            else:
                break

        informacoes_vendas["PRECO"] = produto_escolhido["PRECO"]
        informacoes_vendas["NOME"] = produto_escolhido ["NOME"]
        informacoes_vendas["TOTAL"] = informacoes_vendas["QTD"]*informacoes_vendas["PRECO"]
        informacoes_vendas["ID"] = produto_escolhido["ID"]
        informacoes_vendas["DATA"] = (f'{agora.tm_mday}/{agora.tm_mon}/{agora.tm_year}')
        produto_escolhido["QTD"] -=informacoes_vendas["QTD"]
        while True:
            continuar = input('Deseja adcionar mais Produtos: [S/N]: ').strip().upper()
            if continuar not in('S','N'):
                continue
            if continuar == 'S':
                nota_fiscal.append(informacoes_vendas.copy())
                break
            if continuar == 'N':
                while True:
                    cpf_nota = input('Deseja adcionar CPF na Nota: [S/N]: ').strip().upper()
                    if cpf_nota not in ('S','N'):
                        continue
                    if cpf_nota == 'S':

                        while True:
                            try:
                                informacoes_vendas["CPF"] = int(input('Digite o CPF: ')) # TRATAMENTO DE ERROS
                                cpf_string=str(informacoes_vendas["CPF"])
                                if len(cpf_string)!=11:
                                    print('CPF Inválido, Favor digitar um CPF existente !')
                                    time.sleep(1.5)
                                    continue
                            except ValueError:
                                print('Favor digitar somente Números !')
                                time.sleep(1.5)
                            else:
                                break

                    else:
                        informacoes_vendas["CPF"] = "Não Incluso"
                    for item in nota_fiscal:
                        item["CPF"] = informacoes_vendas["CPF"]
                    nota_fiscal.append(informacoes_vendas.copy())
                    dados_venda.append(nota_fiscal[:])
                    break
            if continuar == 'N':
                break
        if continuar == 'N':
            break

            
            
def listar_venda(informacao,nota_fiscal):
    total =0
    print(f'{'='*84}\n\n{'ID':^8}{'NOME':^53}{'PREÇO':^13}{'QTD':^8}\n')
    for compra in nota_fiscal:
        print(f'{compra["ID"]:^8}'
            f'{compra["NOME"][:35]:^53}'
            f'{compra["PRECO"]:^13.2f}'
            f'{compra["QTD"]:^8}')
        total += compra["PRECO"]*compra["QTD"]
        time.sleep(0.15)
    print('')
    print(f'TOTAL: {total:.2f}\n'
    f'CPF: {compra["CPF"]}')
    nota_fiscal.clear()

def gerar_relatorio(informacao, dados, caminho_arquivo):
    if dados == []:
        with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(f"{'=-'*15}{' Relatório de Vendas '}{'-='*15}\n\n")
            arquivo.write(f"{'Você ainda não fez nenhuma venda.':^82}")
    else:
        with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(f"{'=-'*15}{' Relatório de Vendas '}{'-='*15}\n\n")
            arquivo.write(f"{'='*81}\n\n{'ID':^8}{'NOME':^45}{'PREÇO':^13}{'QTD':^8}{'TOTAL':^8}\n\n")
            total_relatorio = 0
            for compras in dados:
                total_compra = 0
                cpf = "Não Informado"
                for produto in compras:
                    total_compra += produto["TOTAL"]
                    cpf = produto["CPF"]  
                    arquivo.write(f"{produto['ID']:^8}{produto['NOME'][:35]:^46}{produto['PRECO']:^12.2f}{produto['QTD']:^8}{produto['TOTAL']:^8.2f}\n")
                total_relatorio+=total_compra
                arquivo.write(f"\nDATA: {produto["DATA"]}\nCPF: {cpf}\nTOTAL: {total_compra:.2f}\n\n")
            arquivo.write(f'{'='*81}')
            arquivo.write(f'\n\nTOTAL DO RELATÓRIO: {total_relatorio:.2f}\n')
            arquivo.write(f'VENDAS FEITAS: {len(dados)}')

    print("Relatório Gerado com Sucesso!")


def restaurar_relatorio(informacoes,dados,VENDAS):
    dados.clear()
