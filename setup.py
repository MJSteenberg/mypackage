from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="0.1",
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA - TEAM9 Predict Package',
    long_description=open('README.md').read(),
    install_requires=['numpy','pandas'],
    url='https://github.com/MJSteenberg/mypackage',
    author='MJSteenberg',
    author_email='mjsteenberg01@icloud.com'
)
