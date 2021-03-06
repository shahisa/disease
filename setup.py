# As outlined in https://packaging.python.org/distributing/ 
# this is the setup.py file. This is for creating the pip 
# module

name = 'disease'
version = '0.0.1'
description = 'A python extractor that takes disease names from URL or text'
url = "https://github.com/shahisa/disease"
author = 'Isa Weaver'
authorEmail = 'isaiahweaver@protonmail.com'
license = 'MIT'
install_requires = ['nltk','newspaper']
packages = setuptools.find_packages

setup()

#In the georgrapy project this file was absent completely, however it was 
# definatly in use because of the alerts for installing jellyfish and newspaper
# There must be way to hide this file. 