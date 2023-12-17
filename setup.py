from setuptools import setup, find_packages
setup(name="census-income",
      version="0.0.1",
      author='Vishu',
      author_email="vishwamohansinghnegi@gmail.com",
      packeges=find_packages(),
      install_requires=["pandas","numpy","flask"]
      )