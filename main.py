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

# Get last two CSV files and their Names
def get_two_CSV_files():
  dir = os.path.join(os.getcwd(), "Planilhas")
  files = sorted(os.listdir(dir))
  last_df = pd.read_csv(os.path.join(dir, files[-1]))
  second_last_df = pd.read_csv(os.path.join(dir, files[-2]))
  return last_df, second_last_df, files[-2], files[-1]

# Return symmetric difference between two DataFrames
def dataframe_difference(df1, df2):
    comparison_df = df1.merge(df2, indicator=True, how='outer')
    first_only_df = comparison_df[comparison_df['_merge'] == 'right_only']
    second_only_df = comparison_df[comparison_df['_merge'] == 'left_only']
    first_only_df = first_only_df.reset_index(drop=True)
    second_only_df = second_only_df.reset_index(drop=True)
    del first_only_df['_merge']
    del second_only_df['_merge']
    c = pd.DataFrame.equals(first_only_df, second_only_df)
    return first_only_df, second_only_df, c

# Print difference between Dataframes A and B
def print_df_differences(A, B):
  print("---> 1. Versão do Banco de Dados:\n")
  print(A)
  print("\n---> 2. Versão Recentemente Inserida:\n")
  print(B)
  print("\n--> Obs.: NaN significa que a célula está vazia.")

# Update Database
def update_file(A, B, A_name, B_name, c):
  print_df_differences(A, B)
  dir = os.path.join(os.getcwd(), "Planilhas")
  while True:
    c = str(input("\n---> Qual versão deseja manter? (1 ou 2): "))
    if c == '1':
      os.remove(os.path.join(dir, B_name))
    elif c == '2':
      os.remove(os.path.join(dir, A_name))
      os.rename(os.path.join(dir, B_name), A_name)
    else:
      print("\n---> Valor inválido!")
    if (c == '1') or (c == '2'):
      break
    

# Check for duplicate files
def check_for_duplicates(A, B, A_name, B_name, c):
  if c == True:
    os.remove(os.path.join(os.getcwd(), "Planilhas", B_name))
  else:
    update_file(A, B, A_name, B_name, c)

def update_database():
  A, B, A_name, B_name = get_two_CSV_files()
  A, B, c = dataframe_difference(A, B)
  check_for_duplicates(A, B, A_name, B_name, c)

# Iniciar Programa
def main():
  #save_CSV(read_spreadsheet(extract_ID()))
  update_database()

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
# 3 - (x) CRIAR UMA FUNÇÃO PARA DETECTAR SE O ARQUIVO DE ÍNDICE N+1, GERADO NA ÚLTIMA EXECUÇÃO, É INDÊNTICO AO ARQUIVO DE ÍNDICE N, ATRAVÉS DA FUNÇÃO check_for_duplicates().
# 4 - (X) CRIAR UMA FUNÇÃO update_file() PARA ATUAR EM DOIS ARQUIVOS, UM DE ÍNDICE N E OUTRO DE ÍNDICE N+1, QUE TENHA O SEGUINTE COMPORTAMENTO:
#  4-1 (x) SE O ARQUIVO DE ÍNDICE N+1 FOR IDÊNTICO AO ARQUIVO DE ÍNDICE N, DELETAR O ARQUIVO DE ÍNDICE N+1
#  4-2 (X) SE HOUVER ALTERAÇÕES, SALVAR TAIS ALTERAÇÕES EM UM ARQUIVO DE TEXTO SEGUNDO O MODELO:
#    - Current version: [...]
#    - Latest version:  [...]
#  4-3 (X) CRIAR UMA FUNÇÃO PARA EXIBIR CONTEÚDO DO ARQUIVOD E TEXTO E PERGUNTAR SE O USUÁRIO DESEJA SALVAR A VERSÃO MAIS NOVAS OU DESCARTÁ-LA. 

'''
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
'''