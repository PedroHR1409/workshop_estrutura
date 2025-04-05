"""
Este módulo implementa o pipeline ETL de dados.

Ele extrai os dados de arquivos Excel de uma pasta especificada,
transforma esses dados através da concatenação de múltiplos DataFrames
e, em seguida, carrega os dados transformados em um arquivo Excel de saída.

Funções:
- pipeline_completa(
    input_folder: str,
    output_folder: str,
    output_file_name: str):
    Executa o processo completo de ETL: extrai, transforma e carrega os dados.
"""

from src.pipeline.transform import concat_from_list
from src.pipeline.extract import extract_files
from src.pipeline.load import save_df


def pipeline_completa(input_folder, output_folder, output_file_name):
    """
    Função ETL: extrai, transforma e carrega dados de arquivos Excel.

    args:
        input_folder (str): Caminho da pasta de entrada com arquivos Excel.
        output_folder (str): Caminho da pasta de saída onde o arquivo
        consolidado será salvo.
        output_file_name (str): Nome do arquivo Excel de saída.

    returns:
        None
    """
    dfs = extract_files(input_folder)
    df_merged = concat_from_list(dfs)
    save_df(df_merged, output_folder, output_file_name)
