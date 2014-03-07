from distutils.core import setup

version = '0.1.0'

setup(
    name='passes',
    version=version,
    discription='',
    license='BSD',

    long_description='',
    author='Esben Sonne',
    author_email='esbensonne@gmail.com',

    packages='',
    entry_points={
        'console_scripts': [
            'passes = passes.cli:main'
        ],
    },

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Auditence :: Developers',
    ],
)
