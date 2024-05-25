from setuptools import setup, find_packages

setup(
    name='csv_to_sql',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
    ],
)