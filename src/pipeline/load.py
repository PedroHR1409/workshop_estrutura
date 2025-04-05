import os

import pandas as pd


def save_df(df: pd.DataFrame, folder: str, file_name: str) -> None:
    """
    Função para salvar o DataFrame no caminho informado
    """
    os.makedirs(folder, exist_ok=True)

    if not file_name.endswith('.xlsx'):
        file_name += '.xlsx'

    file_path = os.path.join(folder, file_name)
    df.to_excel(file_path, index=False)
    return file_path
