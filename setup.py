#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Flask-KeyVault
-------------------

Flask extension to read and write secrets from Azure Key Vault
"""
import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()
exec((HERE / "flask_keyvault/version.py").read_text())

setup(
    name='Flask-KeyVault',
    version=__version__,
    url='https://github.com/erikhoward/flask-keyvault',
    license='MIT',
    author='Erik Howard',
    author_email="erikhoward@protonmail.com",
    description='Flask extension to read and write secrets from Azure Key Vault',
    long_description=README,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    keywords=["flask", "azure", "keyvault", "secrets"],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'azure-keyvault'
    ],
    test_suite='tests',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
