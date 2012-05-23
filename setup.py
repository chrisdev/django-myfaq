import codecs
import os
import sys
from setuptools import setup, find_packages

def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()


PACKAGE = "faq"
NAME = "django-myfaq"
DESCRIPTION = "An independent fork of django-faq by Kevin Fricovsky that we use in some of our projects"
AUTHOR = "Chris Clarke"
AUTHOR_EMAIL = "cclarke@chrisdev.com"
URL = "http://github.com/chrisdev/pinax-theme-foundation"
VERSION = __import__(PACKAGE).__version__


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=read('README.rst'),
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="MIT",
    url=URL,
    packages=find_packages(exclude=["tests.*", "tests","example_project"]),
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ],
    zip_safe=False,
)
