from pipeline.extract import extract_files
from pipeline.load import save_df
from pipeline.transform import concat_from_list

if __name__ == '__main__':
    dfs = extract_files('./data/input')
    df_merged = concat_from_list(dfs)
    
    save_df(df_merged, 'data/output/consolidated_data.xlsx')
