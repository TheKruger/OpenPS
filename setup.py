from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='OpenPS',
   version='0.0.1',
   description='Open source plugin system.',
   long_description=long_description,
   author='TheKruger',
   keywords=["python", "plugin-system"],
   packages=['OpenPS']
)
