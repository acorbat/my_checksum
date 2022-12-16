import pandas as pd
import pathlib
from simple_file_checksum import get_checksum
import sys
from tqdm import tqdm


DATA_DIR = pathlib.Path(sys.argv[1])

file_list = [filepath for filepath in DATA_DIR.rglob("*") if filepath.is_file()]

hash_dict = pd.DataFrame.from_dict({str(filepath): get_checksum(filepath) for filepath in tqdm(file_list)},
                                   orient="index", columns=['hash_value'])
hash_dict.index.name = 'filepath'
save_path = DATA_DIR if DATA_DIR.is_dir() else DATA_DIR.parent
save_path = save_path / hash_dict.xlsx
hash_dict.to_excel(save_path)
