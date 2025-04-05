"""
Este módulo contém funções para extrair dados de arquivos Excel.

A função principal, `extract_files`, lê os arquivos `.xlsx` da pasta fornecida
e retorna uma lista de DataFrames.

Funções:
- extract_files(folder_path: str) -> List[pd.DataFrame]: Lê todos os arquivos
Excel em uma pasta e retorna uma lista de DataFrames.
"""

import glob
import os
from typing import List

import pandas as pd

"""Funções para extrair dados"""


def extract_files(folder_path: str) -> List[pd.DataFrame]:
    """
    Função para ler arquivos de uma pasta e retornar uma lista de dataframes.

    args:
        folder_path (str): Caminho da pasta com arquivos

    returns:
        List[pd.DataFrame]: Lista de dataframes lidos dos
        arquivos Excel

    """
    all_files = glob.glob(os.path.join(folder_path, '*.xlsx'))

    dataframe_list = []

    for file in all_files:
        dataframe_list.append(pd.read_excel(file))

    return dataframe_list
