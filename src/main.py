from pipeline.extract import extract_files
from pipeline.transform import concat_from_list

dfs = extract_files('./data/input')
df_merged = concat_from_list(dfs)
print(df_merged)
