from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function returns the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()#when line is read then new char will also embedded so
        requirements=[req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements
setup(
    name='mlendtoend',
    version='0.0.1',
    author='akshay',
    author_email='akshaykrishnavarma@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)