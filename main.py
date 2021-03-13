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
#import io

#
##
###
##########################
# 2 - Definição de Funções
##########################
###
##
#

# Extract spreadsheet ID
def extract_ID():
  #URL = input("Insert Public Spreadsheet URL: ")
  URL = "https://docs.google.com/spreadsheets/d/1QtqGEaQuipX9Z1DSc97zCnxxOF-ggkTRrRg7e4ih8c4/edit#gid=0"
  return URL.split('/')[-2]

# Read spreadsheet
def read_spreadsheet(sheet_id):
  return pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")

# Create folder
def make_dir(a):
  dir = os.path.join(os.getcwd(), a)
  if not os.path.exists(dir):
      os.mkdir(dir)

# Find last index
def get_last_index():
  dir = os.path.join(os.getcwd(), "Planilhas")
  a = 1
  while os.path.isfile(os.path.join(dir, str(a) + "-FILE" + ".csv")):
    a = int(a) + 1
  return a

# Save CSV
def save_CSV(df):
  make_dir("Planilhas")
  a = get_last_index()
  save_path = os.path.join(os.getcwd(), "Planilhas")
  completeName = os.path.join(save_path, str(a) + "-FILE" + ".csv")
  df.to_csv (completeName, index = False, header=True)

# Get two last CSV files
def get_two_CSV_files():
  dir = os.path.join(os.getcwd(), "Planilhas")
  files = sorted(os.listdir(dir))
  last_df = pd.read_csv(os.path.join(dir, files[-1]))
  second_last_df = pd.read_csv(os.path.join(dir, files[-2]))
  return last_df, second_last_df

# Return symmetric difference between two DataFrames
def dataframe_difference(df1, df2):
    comparison_df = df1.merge(df2, indicator=True, how='outer')
    first_only_df = comparison_df[comparison_df['_merge'] == 'right_only']
    second_only_df = comparison_df[comparison_df['_merge'] == 'left_only']
    first_only_df = first_only_df.reset_index(drop=True)
    second_only_df = second_only_df.reset_index(drop=True)
    del first_only_df['_merge']
    del second_only_df['_merge']
    return first_only_df, second_only_df

# Print difference between Dataframes A and B
def print_df_differences(A, B):
  print("---> Antigo:\n")
  print(A)
  print("\n---> Novo:\n")
  print(B)
  print("\n--> Obs.: NaN significa que a célula está vazia.")

# Update Database
def update_file():

  #a = check_for_duplicates()
  #if a == 1

  A, B = get_two_CSV_files()
  A, B = dataframe_difference(A, B)
  print_df_differences(A, B)

# Check for duplicate files
def check_for_duplicates():
  
  dir = os.path.join(os.getcwd(), "Planilhas")
  os.chdir(dir)
  files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)

  if files[-1] != "1-FILE.csv":

    before_last = files[-2]
    before_last_csv = str(pd.read_csv(os.path.join(dir, before_last)))
    last = files[-1]
    last_csv = str(pd.read_csv(os.path.join(dir, last)))


    if (before_last_csv == last_csv):
      x = 0
      os.remove(last)
      # new file is a duplicate and won't be saved

    else:
      x = 1
      # new file will proceed to the next function
  
  else:
    x = 0
  return x # (1 = yes, 0 = no)

def menu():
  print("---[ Início do Programa ]---")
  print("\n\n\n(1) main()\n(2) update_file()")
  x = str(input("\n---> Escolha uma função a ser executada: "))
  if x == '1':
    main()
    print("\n----> Função {} executada com sucesso.".format("main()"))
  elif x == '2':
    print("\n")
    update_file()
    print("\n\n---> Função {} executada com sucesso.".format("update_file()"))
  else:
    print("\n---> Valor inválido!")
  print("\n\n\n---[ Fim do Programa ]---")

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

update_file()
#menu()


# 1 - (x) SALVAR OS ARQUIVOS CSV EM UMA PASTA, NÃO NO MESMO DIRETÓRIO DO ARQUIVO PYTHON
# 2 - (x) SE ESTIVER COM O MESMO NOME, NÃO SOBRESCREVER, E SIM SALVAR COM OUTRO NOME (PLANILHA_1 -- > PLANILHA_2)
# 3 - (x) CRIAR UMA FUNÇÃO PARA DETECTAR SE O ARQUIVO DE ÍNDICE N+1, GERADO NA ÚLTIMA EXECUÇÃO, É INDÊNTICO AO ARQUIVO DE ÍNDICE N, ATRAVÉS DA FUNÇÃO check_for_duplicates().
# 4 - ( ) CRIAR UMA FUNÇÃO update_file() PARA ATUAR EM DOIS ARQUIVOS, UM DE ÍNDICE N E OUTRO DE ÍNDICE N+1, QUE TENHA O SEGUINTE COMPORTAMENTO:
#  4-1 (x) SE O ARQUIVO DE ÍNDICE N+1 FOR IDÊNTICO AO ARQUIVO DE ÍNDICE N, DELETAR O ARQUIVO DE ÍNDICE N+1
#  4-2 ( ) SE HOUVER ALTERAÇÕES, SALVAR TAIS ALTERAÇÕES EM UM ARQUIVO DE TEXTO SEGUNDO O MODELO:
#    - Current version: [...]
#    - Latest version:  [...]
#  4-3 ( ) CRIAR UMA FUNÇÃO PARA EXIBIR CONTEÚDO DO ARQUIVOD E TEXTO E PERGUNTAR SE O USUÁRIO DESEJA SALVAR A VERSÃO MAIS NOVAS OU DESCARTÁ-LA. 