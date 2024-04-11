from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

AUTHOR_USER_NAME = "Raguramrrr"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ['streamlit']


setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="A small package for Movie Recommender System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author_email="raguramanraja45@gmail.com",
    packages=[SRC_REPO],
    python_requires=">=3.8",
    install_requires=LIST_OF_REQUIREMENTS
)