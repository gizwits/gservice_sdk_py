from setuptools import setup


setup(name='gservice', 
      version='0.1',
      install_requires=['requests==2.4.3'],
      packages=['gservice', 'gservice.api', 'gservice.calls'],
      test_suite='tests',
)
