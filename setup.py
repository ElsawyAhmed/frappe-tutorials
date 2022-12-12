from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in school_management/__init__.py
from school_management import __version__ as version

setup(
	name="school_management",
	version=version,
	description="training task",
	author="Advintic",
	author_email="sawyahmed951@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
