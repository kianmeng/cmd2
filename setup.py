#!/usr/bin/python
# coding=utf-8
"""
Setuptools setup file, used to install or test 'cmd2'
"""

import codecs

from setuptools import (
    setup,
)

DESCRIPTION = "cmd2 - quickly build feature-rich and user-friendly interactive command line applications in Python"

with codecs.open('README.md', encoding='utf8') as f:
    LONG_DESCRIPTION = f.read()

CLASSIFIERS = list(
    filter(
        None,
        map(
            str.strip,
            """
Development Status :: 5 - Production/Stable
Environment :: Console
Operating System :: OS Independent
Intended Audience :: Developers
Intended Audience :: System Administrators
License :: OSI Approved :: MIT License
Programming Language :: Python
Programming Language :: Python :: 3
Programming Language :: Python :: 3.8
Programming Language :: Python :: 3.9
Programming Language :: Python :: 3.10
Programming Language :: Python :: 3.11
Programming Language :: Python :: 3.12
Programming Language :: Python :: 3.13
Programming Language :: Python :: Implementation :: CPython
Topic :: Software Development :: Libraries :: Python Modules
""".splitlines(),
        ),
    )
)  # noqa: E128

SETUP_REQUIRES = ['setuptools', 'setuptools_scm']

INSTALL_REQUIRES = [
    'pyperclip',
    'wcwidth',
]

EXTRAS_REQUIRE = {
    # Windows also requires pyreadline3 to ensure tab completion works
    ":sys_platform=='win32'": ['pyreadline3'],
    # Extra dependencies for running unit tests
    'test': [
        "gnureadline; sys_platform=='darwin'",  # include gnureadline on macOS to ensure it is available in nox env
        'codecov',
        'coverage',
        'pytest',
        'pytest-cov',
        'pytest-mock',
    ],
    # development only dependencies:  install with 'pip install -e .[dev]'
    'dev': [
        'codecov',
        'doc8',
        'invoke',
        'mypy',
        'nox',
        "pytest>=4.6",
        'pytest-cov',
        'pytest-mock',
        'sphinx',
        'sphinx-rtd-theme',
        'sphinx-autobuild',
        'ruff',
        'twine',
    ],
    'docs': [
        'setuptools',
        'setuptools_scm',
        'sphinx',
        'sphinx-rtd-theme',
        'sphinx-autobuild',
    ],
    'validate': [
        'mypy',
        'ruff',
        'types-setuptools',
    ],
}

PACKAGE_DATA = {
    'cmd2': ['py.typed'],
}

setup(
    name="cmd2",
    use_scm_version={'git_describe_command': 'git describe --dirty --tags --long --exclude plugin-*'},
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    classifiers=CLASSIFIERS,
    author='Catherine Devlin',
    author_email='catherine.devlin@gmail.com',
    url='https://github.com/python-cmd2/cmd2',
    license='MIT',
    platforms=['any'],
    package_data=PACKAGE_DATA,
    packages=['cmd2'],
    keywords='command prompt console cmd',
    python_requires='>=3.8',
    setup_requires=SETUP_REQUIRES,
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
)
