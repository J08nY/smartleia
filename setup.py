
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


import os.path

readme = ''
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, 'README.md')
if os.path.exists(readme_path):
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')


setup(
    long_description=readme,
    name='smartleia',
    version='1.0.1',
    description='Python toolkit for LEIA smartcard reader',
    python_requires='==3.*,>=3.6.0',
    project_urls={"homepage": "https://h2lab.org/devices/leia/quickstart/", "repository": "https://github.com/h2lab/smartleia"},
    author='LEIA Team',
    author_email='leia@h2lab.org',
    license='LGPL-2.1+',
    packages=['smartleia'],
    package_dir={"": "."},
    package_data={"smartleia": ["*.csv", "*.ipynb"]},
    install_requires=['pyserial==3.*,>=3.4.0'],
    extras_require={
        "dev": ["dephell==0.*,>=0.8.3", "black==19.*,>=19.10.0.b0", "bump2version==1.*,>=1.0.0", "coverage==5.*,>=5.1.0", "flake8==3.*,>=3.7.9", "ipython==7.*,>=7.14.0", "mypy==0.*,>=0.770.0", "nbsphinx==0.*,>=0.7.0", "pandoc==1.*,>=1.0.2", "pre-commit==2.*,>=2.3.0", "pylint==2.*,>=2.5.2", "pytest-runner==5.*,>=5.2.0", "recommonmark==0.*,>=0.6.0", "sphinx==3.*,>=3.0.0", "sphinx-autodoc-typehints==1.*,>=1.10.3", "sphinx-rtd-theme==0.*,>=0.5.0", "sphinxcontrib.spelling==5.*,>=5.0.0", "sphinxcontrib.wavedrom==2.*,>=2.1.0"],
        "test": ['pytest==5.*,>=5.2.0', 'pytest-csv==2.*,>=2.0.2']
    },
)
