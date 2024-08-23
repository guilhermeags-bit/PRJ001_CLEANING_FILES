# ==============================================================================
#  Projeto: PRJ001_CLEANING_FILES
#  Versão:  v1.0
#  Autor:   Guilherme Augusto
#  Data:    2024-08-23
# ==============================================================================

"""
Este módulo "main" faz parte do projeto PRJ001_CLEANING_FILES.
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
import configparser
from app import funcao_listador_arquivos, funcao_filtrar_e_excluir

cfg = configparser.ConfigParser()
cfg.read('config.ini')
local_arquivo = cfg.get('CONFIGURACOES', 'local_arquivo')
data_modificacao = cfg.getint('CONFIGURACOES', 'data_modificacao')


def iniciar_programa():
    main = True

    print('==============================================================')
    print('PROGRAMA: PRJ001_CLEANING_FILES')
    print('==============================================================')
    print('VERSÃO: v1.0')
    print('AUTOR: Guilherme Augusto')
    print('DATA DE CRIAÇÃO: 2024-08-23')
    print('--------------------------------------------------------------')
    print('DESCRIÇÃO:')
    print('Este programa realiza a limpeza de arquivos antigos de acordo')
    print('com a data de modificação.')
    print()
    print('Atenção: Não esqueça de configurar o arquivo "config"')
    print('com as configurações desejadas.')
    print('==============================================================\n')

    while main:
        print(f'Data de exclusão: {data_modificacao} dias.\n')
        print(f'Diretório selecionado: {local_arquivo}\n\n')
        print('COMANDOS:')
        print('[1] Listar arquivos no diretório')
        print('[2] Apagar os arquivos')
        print('[3] Sair do programa')
        opcao_usuario = input('[COMANDO]: ')

        if opcao_usuario == '1':
            print()
            funcao_listador_arquivos(local_arquivo, data_modificacao)
            os.system('cls')
        elif opcao_usuario == '2':
            print()
            funcao_filtrar_e_excluir(local_arquivo, data_modificacao)
            os.system('cls')
        elif opcao_usuario == '3':
            main = False
            input('Programa finalizado.\n'
                  'Aperte "enter" para fechar o prompt.')
            os.system('cls')
        else:
            print('Digite uma opção válida!')
            input('Aperte "enter" para fechar o prompt.')
            os.system('cls')


if __name__ == '__main__':
    iniciar_programa()
