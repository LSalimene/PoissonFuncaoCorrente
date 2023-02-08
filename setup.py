from setuptools import setup, find_packages  
with open("README.md", "r") as fh:
    description = fh.read()
  
setup(
    name="PoissonFuncaoCorrente",
    version="1.0.0",
    author="Lucas Salimene",
    author_email="lucassalimene@protonmail.com",
    packages=find_packages(),
    description="Um pacote para o calculo da funcao corrente",
    long_description="Esse pacote utiliza métodos númericos iterativos para resolver a equação que relaciona a Função Corrente com a vorticidade",
    license='MIT',
    long_description_content_type="text/markdown",
    python_requires='>=3.8',
    install_requires=['numpy']
)
