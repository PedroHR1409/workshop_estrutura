import os
import tempfile

import pandas as pd

from src.pipeline.pipeline import pipeline_completa


def test_integration():
    """ """
    with tempfile.TemporaryDirectory() as tmpdirname:
        input_folder = os.path.join(tmpdirname, 'input')
        output_folder = os.path.join(tmpdirname, 'output')
        os.makedirs(input_folder)

        sample_data = pd.DataFrame(
            {'A': list(range(1, 11)), 'B': list('abcdefghij')}
        )
        sample_file_path = os.path.join(input_folder, 'sample.xlsx')
        sample_data.to_excel(sample_file_path, index=False)

        pipeline_completa(input_folder, output_folder, 'consolidated.xlsx')

        output_file_path = os.path.join(output_folder, 'consolidated.xlsx')
        assert os.path.exists(output_file_path)

        loaded_data = pd.read_excel(output_file_path)
        pd.testing.assert_frame_equal(loaded_data, sample_data)
