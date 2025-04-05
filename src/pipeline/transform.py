"""
Este módulo contém funções para manipular e transformar DataFrames.

A função principal, `concat_from_list`, recebe uma lista de DataFrames e
os concatena em um único DataFrame.

Funções:
- concat_from_list(list_with_dfs: list) -> pd.DataFrame:
    Concatena os DataFrames em uma lista em um único DataFrame.
"""

import pandas as pd


def concat_from_list(list_with_dfs: list) -> pd.DataFrame:
    """
    Função para concatenar os dataframes de uma lista.

    args:
        list_with_dfs (list): Lista contendo os DataFrames a serem
        concatenados.

    returns:
        pd.DataFrame: DataFrame resultante da concatenação dos DataFrames
        na lista.
    """
    return pd.concat(list_with_dfs, ignore_index=True)
