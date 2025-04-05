from src.pipeline.transform import concat_from_list
import pandas as pd

df_1 = pd.DataFrame({'col_1': [1,2], 'col_2': [3,4]})
df_2 = pd.DataFrame({'col_1': [5,6], 'col_2': [7,8]})

def test_concat_dfs():
    df = concat_from_list([df_1, df_2])

    assert df.shape == (4,2)