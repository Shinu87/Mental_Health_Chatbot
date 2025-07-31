from setuptools import find_packages,setup

setup(
    name='Mental_Health_Chatbot',
    version='0.1.0',
    author='Shrinivas M',
    author_email = "",
    packages=find_packages(),
    install_requires=[
        'langchain==0.3.26',
        'flask==3.1.1',
        'sentence-transformers==4.1.0',
        'pypdf==5.6.1',
        'langchain-pinecone==0.2.8',
        'langchain-openai==0.3.24',
        'langchain-community==0.3.26'
    ],
)