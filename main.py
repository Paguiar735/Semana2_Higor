#
##
##
###############################
# 1 - Importação de Bibliotecas
###############################
###
##
#

# Bloco de código importante
# Outro bloco de código

import os
import sys
import itertools
import pandas as pd
from urllib.parse import urlparse
from pathlib import Path

#
##
###
##########################
# 2 - Definição de Funções
##########################
###
##
#

# Extrair ID da planilha
def extract_ID():
  #URL = input("Insert Public Spreadsheet URL: ")
  URL = "https://docs.google.com/spreadsheets/d/1QtqGEaQuipX9Z1DSc97zCnxxOF-ggkTRrRg7e4ih8c4/edit#gid=0"
  return URL.split('/')[-2]

# Ler a Planilha
def read_spreadsheet(sheet_id):
  return pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")

# Criar Diretório
def make_dir(a):
  dir = os.path.join(os.getcwd(), a)
  if not os.path.exists(dir):
      os.mkdir(dir)

# Salvar CSV
def save_CSV(df):
  make_dir("Planilhas")
  save_path = os.path.join(os.getcwd(), "Planilhas")
  completeName = os.path.join(save_path, "FILE" + ".csv")
  df.to_csv (completeName, index = False, header=True)

# Iniciar Programa
def main():
  save_CSV(read_spreadsheet(extract_ID()))

#
##
###
########################
# 3 - Início do Programa
########################
###
##
#

main()

'''
# operador para contar o sufixo do arquivo
c = itertools.count()

# ------------ DEMONSTRATIVO ------------ (APAGAR)#
                                                  #
if os.path.exists(completename):                  #
    print("o arquivo ja existe no diretorio:")    #
    print(completename)                           #
else:                                             #
    print("o arquivo é novo nesse diretorio")     #
                                                  #
# ------------------------------------------------#


# sondar o diretorio em busca do nome do arquivo
# enquanto o nome do arquivo existir, c = c + 1
while os.path.exists(completename):
    actualname = "%s (%d).%s" % (filename,next(c),ext)
    completename = os.path.join(save_path, actualname)

# quando o nome for novo no diretorio, salvar arquivo

file1 = open(completename,"w",newline="")
file1.write(df.to_csv(index=False))           # remove o prefixo (0, 1, 2...) da planilha
file1.close()                                 # encerra a edição da planilh


# ------------ DEMONSTRATIVO ------------ (APAGAR)#
                                                  #
print("")                                         #
print("salvando como:")                           #
print(completename)                               #
                                                  #
print("")                                         #
print("arquivo csv salvo:")                       #
print(df.to_string(index=False))                  #
                                                  #
# ------------------------------------------------#


# (x) SALVAR OS ARQUIVOS CSV EM UMA PASTA, NÃO NO MESMO DIRETÓRIO DO ARQUIVO PYTHON
# (x) SE ESTIVER COM O MESMO NOME, NÃO SOBRESCREVER, E SIM SALVAR COM OUTRO NOME (PLANILHA_1 -- > PLANILHA_2)
# ( ) SE HOUVER MODIFICAÇÕES, SALVAR AS MODIFICAÇÕES EM UM ARQUIVO DE TEXTO
'''