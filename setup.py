from setuptools import find_packages, setup

setup(
    name='cy05jv-dataload',
    packages=find_packages(exclude=("tests",)),
    install_requires=[
        "click==7.1.*"
    ],
    extras_require={
        'build': [
            'wheel'
        ],
        'test': [
            'pytest==5.4.*',
            'pyspark==3.1.*'
        ],
        'lint': [
            'flake8==3.8.*',
            'mypy==0.*',
            'pyspark==3.1.*'
        ]
    }
)
