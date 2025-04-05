from src.gpipeline.transform import concat_from_list
from src.pipeline.extract import extract_files
from src.pipeline.load import save_df


def pipeline_completa(input_folder, output_folder, output_file_name):
    """
    Função ETL: extrai, transforma e carrega dados de arquivos Excel.
    """
    dfs = extract_files(input_folder)
    df_merged = concat_from_list(dfs)
    save_df(df_merged, output_folder, output_file_name)
