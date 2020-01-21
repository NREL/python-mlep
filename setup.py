from setuptools import setup

setup(name='mlep',
      version='0.1.dev2',
      description='Interact with an EnergyPlus simulation during runtime using the BCVTB protocol.',
      url='https://github.com/corymosiman12/python-mlep',
      author='Cory Mosiman',
      license='MIT',
      packages=['mlep'],
      long_description=open('README.md').read(),
      install_requires=[
      ])
