from __future__ import print_function
import io
import sys

from setuptools import setup, find_packages


with io.open('README.rst', encoding='utf-8') as readme:
    long_description = readme.read()

# Populates __version__ without importing the package
__version__ = None
execfile('flexget/_version.py')
if not __version__:
    print('Could not find __version__ from flexget/_version.py')
    sys.exit(1)


def load_requirements(filename):
    with io.open(filename, encoding='utf-8') as reqfile:
        return [line.strip() for line in reqfile if not line.startswith('#')]


setup(
    name='FlexGet',
    version=__version__,
    description='FlexGet is a program aimed to automate downloading or processing content (torrents, podcasts, etc.) '
                'from different sources like RSS-feeds, html-pages, various sites and more.',
    long_description=long_description,
    author='Marko Koivusalo',
    author_email='marko.koivusalo@gmail.com',
    license='MIT',
    url='http://flexget.com',
    download_url='http://download.flexget.com',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    test_suite='nose.collector',
    install_requires=load_requirements('requirements.txt'),
    extras_require={
        ':python_version=="2.6"': ['argparse'],
        'dev_tools': load_requirements('dev-requirements.txt')
    },
    entry_points={
        'console_scripts': ['flexget = flexget:main'],
        'gui_scripts': ['flexget-headless = flexget:main']  # This is useful on Windows to avoid a cmd popup
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ]
)
