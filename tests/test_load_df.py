import os
import pandas as pd

from src.pipeline.load import save_df

df_1 = pd.DataFrame({'col_1': [1, 2], 'col_2': [3, 4]})

def test_save_df():
    file_path = save_df(df_1, 'data/output', 'test.xlsx')
    expected_path = os.path.normpath('data/output/test.xlsx')

    assert os.path.normpath(file_path) == expected_path
    assert os.path.exists(file_path)