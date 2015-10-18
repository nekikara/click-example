from setuptools import setup

setup(
    name='example',
    version='0.1',
    py_module=['example'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        example=example:cli
    ''',
)
