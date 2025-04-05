import pandas as pd


def concat_from_list(list_with_dfs: str) -> pd.DataFrame:
    """
    Função para concatenar os dataframes de uma lista

    args: list_with_dfs (str): Lista com dataframes

    returns: DataFrame concatenado

    """
    return pd.concat(list_with_dfs, ignore_index=True)
