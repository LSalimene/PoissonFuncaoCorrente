import setuptools
from setuptools import setup, find_packages  
with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PoissonFuncaoCorrente",
    version="1.1.2",
    author="Lucas Salimene",
    author_email="lucassalimene@protonmail.com",
    description="Um pacote para o calculo da funcao corrente",
    long_description="Esse pacote utiliza métodos númericos iterativos para resolver a equação que relaciona a Função Corrente com a vorticidade",
    long_description_content_type = "text/markdown",
    url = "https://github.com/LSalimene/PoissonFuncaoCorrente",
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages = ["PoissonFuncaoCorrente"],
    python_requires = ">=3.8"
)

