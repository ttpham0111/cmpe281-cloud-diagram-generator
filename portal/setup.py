import os

from setuptools import setup, find_packages

here = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(here, 'requirements.txt')) as f:
    requires = f.read().strip().split()

setup(
    name='app',

    version='1.0.0',

    description='CMPE 281 Portal SPA',

    include_package_data=True,

    packages=find_packages(),

    py_modules=['run_server'],

    install_requires=requires,

    entry_points={
        'console_scripts': [
            'app = run_server:main'
        ]
    }
)
