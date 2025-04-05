"""
Este módulo contém funções para manipular e salvar DataFrames.

A função principal, `save_df`, salva um DataFrame no caminho e nome de arquivo
especificados.

Funções:
- save_df(df: pd.DataFrame, folder: str, file_name: str) -> None: Salva o
DataFrame em um arquivo Excel na pasta especificada.
"""

import os

import pandas as pd


def save_df(df: pd.DataFrame, folder: str, file_name: str) -> None:
    """
    Função para salvar o DataFrame no caminho informado.

    args:
        df (pd.DataFrame): DataFrame a ser salvo.
        folder (str): Caminho da pasta onde o arquivo será salvo.
        file_name (str): Nome do arquivo a ser salvo.

    returns:
        str: Caminho completo do arquivo salvo.
    """
    os.makedirs(folder, exist_ok=True)

    if not file_name.endswith('.xlsx'):
        file_name += '.xlsx'

    file_path = os.path.join(folder, file_name)
    df.to_excel(file_path, index=False)
    return file_path
