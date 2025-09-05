from setuptools import find_packages, setup
from typing import List
#find_packages will also find how many folders to be considered as package (__init__.py)
HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)-> List[str]:
 #list of requiremenets

  requirements=[]
  with open(file_path, 'r') as file_object:
   requirements=file_object.readlines()
   requirements=[i.replace("\n","")for i in requirements]
  
   if HYPEN_E_DOT in requirements:
    requirements.remove(HYPEN_E_DOT)
  return requirements
setup(
name="mlpro",
version='0.0.1',
author='nz',
author_email='nzx786@gmail.com',
packages=find_packages(),  #will go and check how many folder have __init__.py
install_requires=get_requirements("requirements.txt")
)