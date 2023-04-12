from setuptools import setup, find_packages

setup(
    name='Python-OrangeData',
    version='0.0.2',
    packages=find_packages(),
    author='pysashapy',
    install_requires=open('requirements.txt', 'r').read().split()
)
