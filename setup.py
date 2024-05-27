from setuptools import setup, find_packages

setup(
    name='generate_temp_table_sql',
    version='0.3',
    packages=find_packages(),
    install_requires=[
        'pandas',
    ],
    entry_points={
        'console_scripts': [
            'generate-tt-sql=generate_temp_table_sql.cli:main',
        ],
    },
    author='Ryan Waldorf',
    author_email='ryan@ryanwaldorf.com',
    description='A package to generate SQL statements from CSV files',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/generate_temp_table_sql',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
