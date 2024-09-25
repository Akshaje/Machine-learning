from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT ='-e .'
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements=[reg.replace('\n', "") for reg in requirements]

        if HYPEN_E_DOT IN requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements





setup(
name ='Machine learning',
version = '0.0.1',
author = 'Akshada',
author_email = 'akshadajejurkar7@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')
)