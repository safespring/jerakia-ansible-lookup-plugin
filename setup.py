from setuptools import setup,find_packages

setup(
    name='jerakia-ansible',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    description='Package for performing Jerakia lookups using Ansible',
    author='Jon Ander Novella',
    install_requires=[
        'ansible',
        'jerakia>=0.1.8'
    ]
)
