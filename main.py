from src.pipeline.pipeline import pipeline_completa

if __name__ == "__main__":
    input_folder = 'data/input'
    output_folder = 'data/output'
    output_file_name = 'consolidate_data.xlsx'

    try:
        pipeline_completa(input_folder, output_folder, output_file_name)
        print('Pipeline executado com sucesso!')
    except Exception as e:
        print(f'Erro ao executar o pipeline: {e}')