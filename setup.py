from setuptools import setup, find_packages

setup(
    name='app',

    version='1.0.0',

    description='CMPE 281 Portal SPA',

    include_package_data=True,

    packages=find_packages(),

    py_modules=['run_server'],

    install_requires=[
        'flask==0.12',
        'bcrypt==3.1.3'
    ],

    entry_points={
        'console_scripts': [
            'app = run_server:main'
        ]
    }
)
