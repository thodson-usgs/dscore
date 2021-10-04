from setuptools import setup

setup(name='dscore',
      version='0.1',
      description='Decomposed score (D-score)',
      url='https://github.com/USGS-python/dscore',
      author='Timothy Hodson',
      author_email='thodson@usgs.gov',
      license='CC0',
      packages=['dscore'],
      install_requires=[
          'pandas',
          'statsmodels'
      ],
      zip_safe=False)
