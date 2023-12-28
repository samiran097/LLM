## TO INSTALL LOCAL PACKAGES IN MY VIRTUAL ENVIRONMENT

from setuptools import find_packages,setup

setup(
    name = 'mcqgenerator',
    version = '0.0.1',
    author = 'Samiran Adak',
    author_email= 'samiranadak097@gmail.com',
    install_requires = ["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages = find_packages() # It finds the local package from .init file, it will consoder that folder as a package

)