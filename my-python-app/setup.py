from setuptools import setup, find_packages

setup(
    name='python-app',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'flask',
        'pytest',
    ],
    entry_points={
        'console_scripts': [
            'python-app=src.main:main',  # Example entry point
        ],
    },
)
