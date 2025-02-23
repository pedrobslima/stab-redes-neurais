import setuptools

# Load the long_description from README.md
with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="STab",
    version="0.2",
    description="Transformers com Competição Estocástica para Dados Tabulares",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/kindxiaoming/",
    packages=setuptools.find_packages(),
    install_requires=[
    'torch>=2.3',
    'pandas==2.0.1',
    'einops>=0.8',
    'keras4torch'
  ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
