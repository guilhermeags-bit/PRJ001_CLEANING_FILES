# ==============================================================================
#  Projeto: PRJ001_CLEANING_FILES
#  Versão:  v1.0
#  Autor:   Guilherme Augusto
#  Data:    2024-08-22
# ==============================================================================

"""
Este módulo "app" faz parte do projeto PRJ001_CLEANING_FILES.
Ele foi criado em 2024-08-22 por Guilherme Augusto, e atualmente está na versão 1.0.

Histórico de Revisões:
------------------------------------------------------------------------------
v1.0 - 2024-08-22 - Guilherme Augusto
    * Criação do arquivo inicial
    * Validação das funções principais do programa
    * Testes na prática
    * Validação do programa
------------------------------------------------------------------------------
"""

# ==============================================================================
#  Início do código
# ==============================================================================
from config import local_arquivo, data_modificacao
import os
import shutil
from datetime import datetime, timedelta


# Função para listar arquivos e pastas modificados antes de uma data limite
def funcao_listador_arquivos(local_arquivo, data_modificacao):
    try:
        hoje = datetime.now()
        data_limite = hoje - timedelta(days=data_modificacao)  # Define a data limite para verificação

        arquivos_e_pastas_antigos = []
        arquivos_com_40_caracteres = []
        pastas_para_remover = []

        # Percorre as pastas e arquivos no diretório especificado
        for item in os.listdir(local_arquivo):
            caminho_item = os.path.join(local_arquivo, item)
            caminho_sub_pasta = os.path.join(caminho_item, 'int')

            if os.path.isdir(caminho_item):
                for root, dirs, files in os.walk(caminho_sub_pasta, topdown=False):
                    for file_name in files:
                        caminho_completo_arquivo = os.path.join(root, file_name)
                        data_modificacao_item = datetime.fromtimestamp(os.path.getmtime(caminho_completo_arquivo))
                        # Verifica se o arquivo é antigo e tem 40 caracteres no nome
                        if data_modificacao_item < data_limite and len(file_name) == 40:
                            arquivos_e_pastas_antigos.append(caminho_completo_arquivo)
                            arquivos_com_40_caracteres.append(file_name)
                            # Adiciona as pastas para remoção
                            pasta_atual = os.path.dirname(caminho_completo_arquivo)
                            if pasta_atual != local_arquivo:
                                pasta_atual = os.path.dirname(pasta_atual)
                                pastas_para_remover.append(pasta_atual)
                        break

        if len(arquivos_com_40_caracteres) > 0:
            if arquivos_e_pastas_antigos:
                # Exibe a lista de arquivos que atendem aos critérios
                print('Listas de arquivos com o requisito de nome com 40 caracteres:\n')
                for listagem_arquivos in arquivos_com_40_caracteres:
                    print(listagem_arquivos)

                print(f'\nArquivos modificados há mais de {data_modificacao} dias e com 40 caracteres: '
                      f'{len(pastas_para_remover)} pastas.\n\n')
                input('Aperte "enter" para continuar.')
                os.system('cls')
        else:
            print('Não possui nenhum arquivo para listar!\n\n')
            input('Aperte "enter" para continuar.')
            os.system('cls')
    except Exception as e:
        print(f'Erro: {e}')
        input('Operação abortada. \nAperte "enter" para continuar.')
        os.system('cls')


# Função para filtrar e excluir arquivos e pastas com base em critérios específicos
def funcao_filtrar_e_excluir(local_arquivo, data_modificacao):
    try:
        hoje = datetime.now()
        data_limite = hoje - timedelta(days=data_modificacao)  # Define a data limite para verificação

        arquivos_e_pastas_antigos = []
        arquivos_com_40_caracteres = []
        pastas_para_remover = []

        # Percorre as pastas e arquivos no diretório especificado
        for item in os.listdir(local_arquivo):
            caminho_item = os.path.join(local_arquivo, item)
            caminho_sub_pasta = os.path.join(caminho_item, 'int')

            if os.path.isdir(caminho_item):
                for root, dirs, files in os.walk(caminho_sub_pasta, topdown=False):
                    for file_name in files:
                        caminho_completo_arquivo = os.path.join(root, file_name)
                        data_modificacao_item = datetime.fromtimestamp(os.path.getmtime(caminho_completo_arquivo))
                        # Verifica se o arquivo é antigo e tem 40 caracteres no nome
                        if data_modificacao_item < data_limite and len(file_name) == 40:
                            arquivos_e_pastas_antigos.append(caminho_completo_arquivo)
                            arquivos_com_40_caracteres.append(file_name)
                            # Adiciona as pastas para remoção
                            pasta_atual = os.path.dirname(caminho_completo_arquivo)
                            if pasta_atual != local_arquivo:
                                pasta_atual = os.path.dirname(pasta_atual)
                                pastas_para_remover.append(pasta_atual)
                        break

        if arquivos_e_pastas_antigos:
            # Exibe a lista de arquivos que atendem aos critérios
            print('Listas de arquivos com o requisito de nome com 40 caracteres:\n')
            for listagem_arquivos in arquivos_com_40_caracteres:
                print(listagem_arquivos)

            print(f'\nArquivos modificados há mais de {data_modificacao} dias e com 40 caracteres: '
                  f'{len(pastas_para_remover)} pastas.\n\n')

            # Solicita confirmação do utilizador antes de excluir as pastas
            print('Deseja realmente apagar as respectivas pastas?')
            opcao_usuario = input('COMANDO [Y]Sim [N]Não: ')

            if opcao_usuario in ['Y', 'y']:
                # Ordena as pastas para remover da mais interna para a mais externa
                pastas_para_remover = sorted(pastas_para_remover, reverse=True)
                for pasta in pastas_para_remover:
                    try:
                        shutil.rmtree(pasta)  # Remove a pasta e todo o seu conteúdo
                        print(f'Pasta removida: {pasta}')
                    except Exception as e:
                        print(f'Erro ao remover {pasta}: {e}')

                print("\nArquivos com exatamente 40 caracteres e modificados há mais de", data_modificacao,
                      "dias foram excluídos.\n\n")

                print(f'Todos os arquivos e suas pastas foram deletados.\n')
                input('Aperte "enter" para continuar.')
                os.system('cls')

            elif opcao_usuario in ['N', 'n']:
                print('Operação abortada!\n\n')
                input('Aperte "enter" para continuar.')
                os.system('cls')
            else:
                print('Selecione uma opção válida!\n')
                input('Operação abortada. Aperte "enter" para continuar.')
        else:
            print('Não possui arquivos para listar e excluir.\n\n')
            input('Operação abortada.\nAperte "enter" para continuar.')
    except Exception as e:
        print(f'Erro: {e}')
        input('Operação abortada. \nAperte "enter" para continuar.')
        os.system('cls')


# Ponto de entrada principal do script
if __name__ == '__main__':
    # funcao_filtrar_e_excluir(local_arquivo, data_modificacao)
    funcao_listador_arquivos(local_arquivo, data_modificacao)
    # contar_letras_nome_arquivo(local_arquivo)
