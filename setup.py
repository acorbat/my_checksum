from setuptools import setup, find_packages

setup(
    name='my_checksum',
    version='0.1',
    packages=find_packages(),
    url='https://github.com/acorbat/my_checksum/tree/master/my_checksum',
    license='MIT',
    author='Agustin Corbat',
    author_email='agustin.corbat@ki.se',
    description='Generate an excelsheet with the MD5 checksum of all files inside the provided path.',
    install_requires=['pandas', 'tqdm', 'simple_file_checksum']
)