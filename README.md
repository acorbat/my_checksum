# my_checksum

Generate an excelsheet with the MD5 checksum of all files inside the provided path. The Excel file will have acolumn for the relative filepath and another one for the result of the checksum.

## Usage

Generate a new environment and install the requirements through pip. Download the package or go to my_checksum location and run

"""
python .\my_checksum.py 'C:\path\to\folder'
"""

It will generate a hash_dict.xlsx file inside that folder with the results.
