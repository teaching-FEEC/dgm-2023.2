from setuptools import setup, find_packages

setup(
    name='acgan_ham10000',
    version='0.1.0',
    packages=find_packages(include=['src', 'src.*']),
    install_requires=[
        'torch==2.0.1',
        'numpy==1.23.5',
    ]
)