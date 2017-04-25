from setuptools import setup, find_packages

requires = [
    'boto3>=1.2.3',
]

classifiers = [
    'Environment :: Console',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3'
]

setup(
    name='awsresouceslimit',
    author='Ali Ikram',
    author_email='aikram24@hotmail.com',
    packages=find_packages(),
    install_requires=requires,
    classifiers=classifiers
)
