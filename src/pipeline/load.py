import pandas as pd

def save_df(df: pd.DataFrame, folder: str, file_name: str) -> None:
    """
    Função para salvar o DataFrame no caminho informado
    """
    df.to_excel(f'{folder}/{file_name}.xlsx', index=False)