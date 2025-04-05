import pandas as pd

def save_df(df: pd.DataFrame, folder: str) -> None:
    """
    Função para salvar o DataFrame no caminho informado
    """
    return df.to_excel(folder, index=False, header=True)