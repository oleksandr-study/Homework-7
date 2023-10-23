from setuptools import setup

setup(name = "clean_folder",
      version = "1.0.0",
      description='Sort temp folder',
      author='Oleksandr Velychko',
      url='https://github.com/oleksandr-study/Homework-7',
      licence = "MIT",
      entry_points = {"console_scripts": ["clean-folder = clean_folder.homework7:foldersearch"]})