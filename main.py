"""
Este módulo executa o pipeline de processamento de dados.

Carregando os dados da pasta de entrada e gerando um arquivo consolidado
na pasta de saída.

As pastas de entrada e saída e o nome do arquivo de saída são definidos
como variáveis no código.
O processo é realizado pela função 'pipeline_completa', que é chamada dentro
do bloco principal.

Dependências:
- src.pipeline.pipeline: Função pipeline_completa
"""
from src.pipeline.pipeline import pipeline_completa

"""Arquivo onde o projeto é executado"""
if __name__ == '__main__':
    """Função de execução do projeto"""
    input_folder = 'data/input'
    output_folder = 'data/output'
    output_file_name = 'consolidated_data.xlsx'

    try:
        pipeline_completa(input_folder, output_folder, output_file_name)
        print('Pipeline executado com sucesso!')
    except Exception as e:
        print(f'Erro ao executar o pipeline: {e}')
