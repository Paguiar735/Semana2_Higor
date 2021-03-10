#
##
##
###############################
# 1 - Importação de Bibliotecas
###############################
###
##
#

import os
import pandas as pd

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

# Encontrar último Índice
def get_last_index():
  dir = os.path.join(os.getcwd(), "Planilhas")
  a = 1
  while os.path.isfile(os.path.join(dir, str(a) + "-FILE" + ".csv")):
    a = int(a) + 1
  return a

# Salvar CSV
def save_CSV(df):
  make_dir("Planilhas")
  a = get_last_index()
  save_path = os.path.join(os.getcwd(), "Planilhas")
  completeName = os.path.join(save_path, str(a) + "-FILE" + ".csv")
  df.to_csv (completeName, index = False, header=True)

# Check for duplicate files
def check_for_duplicates():
  
  dir = os.path.join(os.getcwd(), "Planilhas")

  os.chdir(dir)
  files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)

  before_last = files[-2]
  before_last_csv = pd.read_csv(os.path.join(dir, before_last))
  last = files[-1]
  last_csv = pd.read_csv(os.path.join(dir, last))

  print ("Before last file:  ", before_last)
  print ("Last file:         ", last)

  print(before_last_csv)
  print(last_csv)

#  if (before_last_csv == last_csv):
#    print("they are the same")
#  else:
#    print("they are different")


# Iniciar Programa
def main():
  save_CSV(read_spreadsheet(extract_ID()))
  check_for_duplicates()


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

# 1 - (x) SALVAR OS ARQUIVOS CSV EM UMA PASTA, NÃO NO MESMO DIRETÓRIO DO ARQUIVO PYTHON
# 2 - (x) SE ESTIVER COM O MESMO NOME, NÃO SOBRESCREVER, E SIM SALVAR COM OUTRO NOME (PLANILHA_1 -- > PLANILHA_2)
# 3 - ( ) SE HOUVER MODIFICAÇÕES, SALVAR AS MODIFICAÇÕES EM UM ARQUIVO DE TEXTO