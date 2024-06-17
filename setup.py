from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path:str)->List[str]:
    '''
    This function returns a list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines() #reads \n 
        requirements = [req.replace("\n","") for req in requirements]
        
    return requirements
setup(
    name='mlproject',
    version='0.0.1',
    author='Raksha',
    author_email='shreeraksha.mrao@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
