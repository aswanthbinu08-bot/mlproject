from setuptools import find_packages, setup

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> list[str]:
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()

    requirements = [req.strip() for req in requirements]

    requirements = [
        req for req in requirements
        if req and req != HYPEN_E_DOT
    ]

    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='aswanth',
    author_email='aswanth08@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)