from setuptools import find_packages, setup
from typing import List
def get_requirements(file_path:str) -> List[str]:
    '''This function will return the list of requirements
    '''
    HYPEN_E_DOT = '-e .'
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace("\n","").strip() for req in requirements]
    
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
        
    return requirements

setup(
    name="mlpro",
    version="0.1.0",
    author="Prarthana",
    author_email="prarthanajeevan27@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)