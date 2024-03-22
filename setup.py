#!/usr/bin/env python
from setuptools import setup

# https://packaging.python.org/discussions/install-requires-vs-requirements/
install_requires = [
    'termcolor',
    'rsxml',
    'argparse',
]

with open("README.md", "rb") as f:
    long_descr = f.read().decode("utf-8")

version = '0.0.1'

setup(name='riverscapesdemo',
      version=version,
      description='Riverscapes API Demo',
      author='Matt Reimer',
      license='MIT',
      python_requires='>3.5.2',
      long_description=long_descr,
      author_email='info@northarrowresearch.com',
      install_requires=install_requires,
      zip_safe=False,
      packages=[
          'riverscapesdemo'
      ]
      )
