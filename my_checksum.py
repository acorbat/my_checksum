from multiprocessing import Pool
import pandas as pd
import pathlib
from simple_file_checksum import get_checksum
import sys
from tqdm import tqdm


DATA_DIR = pathlib.Path(sys.argv[1])


def make_small_df(filepath):
    rel_filepath = pathlib.Path(filepath).relative_to(DATA_DIR)
    small_hash_df = pd.DataFrame.from_dict({str(rel_filepath): get_checksum(filepath)},
                                           orient="index", columns=['hash_value'])
    small_hash_df.index.name = 'filepath'
    return small_hash_df


if __name__ == '__main__':
    file_list = [filepath for filepath in DATA_DIR.rglob("*") if filepath.is_file()]

    with Pool(14) as p:
        hash_dict = list(tqdm(p.imap_unordered(make_small_df, file_list), total=len(file_list)))
    hash_dict = pd.concat(hash_dict)

    save_path = DATA_DIR if DATA_DIR.is_dir() else DATA_DIR.parent
    save_path = save_path / "hash_dict.xlsx"
    hash_dict.to_excel(save_path)
