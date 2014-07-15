from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='tostadaspipo',
      version=version,
      description="Ejemplo de conju",
      long_description="""\
Ejemplo de conjuntos de tostadas pipo, para demostrar como crear un paquete Egg Python""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='package python egg conjuntos tostadas pipo',
      author='Carlos Malav\xc3\xa9',
      author_email='hellfish2@gmail.com',
      url='https://github.com/hellfish2/tostadaspipo',
      license='GPL 2v',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
