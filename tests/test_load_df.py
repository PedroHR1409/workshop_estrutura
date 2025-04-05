import pandas as pd

from src.pipeline.load import save_df

df_1 = pd.DataFrame({'col_1': [1, 2], 'col_2': [3, 4]})

def test_save_df():
    assert save_df(df_1, './test.xlsx')