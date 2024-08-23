# ==============================================================================
#  Projeto: PRJ001_CLEANING_FILES
#  Versão:  v1.0
#  Autor:   Guilherme Augusto
#  Data:    2024-08-23
# ==============================================================================

"""
Este módulo "app" faz parte do projeto PRJ001_CLEANING_FILES.
Ele foi criado em 2024-08-23 por Guilherme Augusto, e atualmente está na versão 1.0.

Histórico de Revisões:
------------------------------------------------------------------------------
v1.0 - 2024-08-23 - Guilherme Augusto
    * Criação do arquivo inicial
    * Validação das funções principais do programa
    * Testes na prática
    * Validação do programa
------------------------------------------------------------------------------
"""

# ==============================================================================
#  Início do código
# ==============================================================================
import os
import shutil
from datetime import datetime, timedelta
import configparser

cfg = configparser.ConfigParser()
cfg.read('config.ini')
local_arquivo = cfg.get('CONFIGURACOES', 'local_arquivo')
data_modificacao = cfg.getint('CONFIGURACOES', 'data_modificacao')


# Função para listar arquivos e pastas modificados antes de uma data limite
def funcao_listador_arquivos(local_arquivo, data_modificacao):
    try:
        hoje = datetime.now()
        data_limite = hoje - timedelta(days=data_modificacao)  # Define a data limite para verificação

        arquivo_informacoes_apagar = []
        arquivos_e_pastas_antigos = []
        arquivos_com_40_caracteres = []
        pastas_para_remover = set()

        # Coleta arquivos e pastas que precisam ser excluídos
        for item in os.listdir(local_arquivo):
            caminho_item = os.path.join(local_arquivo, item)
            caminho_sub_pasta = os.path.join(caminho_item, 'int')

            if os.path.isdir(caminho_item):
                for root, dirs, files in os.walk(caminho_sub_pasta, topdown=False):
                    for file_name in files:
                        caminho_completo_arquivo = os.path.join(root, file_name)
                        data_modificacao_item = datetime.fromtimestamp(os.path.getmtime(caminho_completo_arquivo))
                        if data_modificacao_item < data_limite and len(file_name) == 40:
                            arquivos_e_pastas_antigos.append(caminho_completo_arquivo)
                            arquivos_com_40_caracteres.append(file_name)
                            pasta_atual = os.path.dirname(caminho_completo_arquivo)
                            for item_informacoes in os.listdir(caminho_item):
                                if item_informacoes == 'Informacoes.txt':
                                    item_informacoes_apagar = f'{caminho_item}\\{item_informacoes}'
                                    arquivo_informacoes_apagar.append(item_informacoes_apagar)
                            while pasta_atual != local_arquivo:
                                pastas_para_remover.add(pasta_atual)
                                pasta_atual = os.path.dirname(pasta_atual)
                            pastas_para_remover.add(caminho_sub_pasta)  # Adiciona a própria pasta 'int'

        print('Listas de arquivos para exclusão:\n')

        if len(arquivo_informacoes_apagar) > 0:
            for listagem_arquivos_informacoes in arquivo_informacoes_apagar:
                print(listagem_arquivos_informacoes)
        else:
            print('Nenhum arquivo de informações.txt para listar.')

        if len(arquivos_e_pastas_antigos) > 0:
            for listagem_arquivos in arquivos_e_pastas_antigos:
                print(listagem_arquivos)
            print(f'\nArquivos modificados há mais de {data_modificacao} dias e com 40 caracteres: '
                  f'{len(arquivos_com_40_caracteres)} arquivos.')
            input('Aperte "enter" para continuar.')
            os.system('cls')
        else:
            print('Nenhum arquivo com 40 caracteres para listar.\n')
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

        arquivo_informacoes_apagar = []
        arquivos_e_pastas_antigos = []
        arquivos_com_40_caracteres = []
        pastas_para_remover = set()

        # Coleta arquivos e pastas que precisam ser excluídos
        for item in os.listdir(local_arquivo):
            caminho_item = os.path.join(local_arquivo, item)
            caminho_sub_pasta = os.path.join(caminho_item, 'int')

            if os.path.isdir(caminho_item):
                for root, dirs, files in os.walk(caminho_sub_pasta, topdown=False):
                    for file_name in files:
                        caminho_completo_arquivo = os.path.join(root, file_name)
                        data_modificacao_item = datetime.fromtimestamp(os.path.getmtime(caminho_completo_arquivo))
                        if data_modificacao_item < data_limite and len(file_name) == 40:
                            arquivos_e_pastas_antigos.append(caminho_completo_arquivo)
                            arquivos_com_40_caracteres.append(file_name)
                            pasta_atual = os.path.dirname(caminho_completo_arquivo)
                            for item_informacoes in os.listdir(caminho_item):
                                if item_informacoes == 'Informacoes.txt':
                                    item_informacoes_apagar = f'{caminho_item}\\{item_informacoes}'
                                    arquivo_informacoes_apagar.append(item_informacoes_apagar)
                            while pasta_atual != local_arquivo:
                                pastas_para_remover.add(pasta_atual)
                                pasta_atual = os.path.dirname(pasta_atual)
                            pastas_para_remover.add(caminho_sub_pasta)  # Adiciona a própria pasta 'int'

        if len(arquivos_com_40_caracteres) > 0:
            print('Listas de arquivos para exclusão:\n')
            for listagem_arquivos in arquivos_com_40_caracteres:
                print(listagem_arquivos)

            print(f'Arquivos modificados há mais de {data_modificacao} dias e com 40 caracteres: '
                  f'{len(arquivos_com_40_caracteres)} arquivos.\n\n')

            print('Deseja realmente apagar os arquivos e suas respectivas pastas?')
            opcao_usuario = input('COMANDO [Y]Sim [N]Não: ')

            if opcao_usuario in ['Y', 'y']:
                # Apagar arquivos
                for caminho_arquivo in arquivos_e_pastas_antigos:
                    try:
                        if os.path.exists(caminho_arquivo):
                            os.remove(caminho_arquivo)
                            print(f'Arquivo removido: {caminho_arquivo}')
                    except Exception as e:
                        print(f'Erro ao remover {caminho_arquivo}: {e}')
                for deletanto_informacoes_iterando in arquivo_informacoes_apagar:
                    try:
                        if os.path.exists(deletanto_informacoes_iterando):
                            os.remove(deletanto_informacoes_iterando)
                            print(f'Arquivo removido: {deletanto_informacoes_iterando}')
                    except Exception as e:
                        print(f'Erro ao remover {deletanto_informacoes_iterando}: {e}')

                print(f'\nTodos os arquivos e suas pastas foram deletados.')
                input('Aperte "enter" para continuar.')
                os.system('cls')

            elif opcao_usuario in ['N', 'n']:
                print('\nOperação abortada!\n\n')
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
    funcao_filtrar_e_excluir(local_arquivo, data_modificacao)
    # funcao_listador_arquivos(local_arquivo, data_modificacao)
    # contar_letras_nome_arquivo(local_arquivo)
