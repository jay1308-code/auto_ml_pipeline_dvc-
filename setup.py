from setuptools import setup,find_packages

with  open("README.md","r",encoding="utf-8") as f:
    long_description=f.read()

setup(
    name="src",
    version="0.0.1",
    author="jay1308",
    description="A SMALL PACKAGE FOR DVC ML PIPELINE DEMO",
    long_description=long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/jay1308-code/auto_ml_pipeline_dvc-",
    author_email="jpandya065@gmail.com",
    package_dir={"":"src"},
    packages=find_packages(where="src"),
    python_requires = ">=3.6"
    install_requires=[
        "dvc",
        "dvc[gdrive]",
        "dvc[s3]",
        "pandas",
        "scikit-learn"
    ]
)