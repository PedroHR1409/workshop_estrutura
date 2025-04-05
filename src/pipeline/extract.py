import glob
import os
from typing import List

import pandas as pd


def extract_files(folder_path: str) -> List[pd.DataFrame]:
    """
    Função para ler os arquivos de uma pasta data/input
    e retornar uma lista de dataframes

    args: folder_path (str): Caminho da pasta com arquivos

    returns: Lista de dataframes

    """
    all_files = glob.glob(os.path.join(folder_path, '*.xlsx'))

    dataframe_list = []

    for file in all_files:
        dataframe_list.append(pd.read_excel(file))

    return dataframe_list
