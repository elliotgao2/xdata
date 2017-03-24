from setuptools import setup

import xdata

setup(
    name=xdata.__name__,
    version=xdata.__version__,
    author="gaojiuli",
    author_email="gaojiuli@gmail.com",
    description="Simple data validation library",
    license="MIT",
    keywords="schema json validation",
    url="https://github.com/gaojiuli/xdata",
    py_modules=['xdata'],
    platforms='any',
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Utilities",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: PyPy",
        "License :: OSI Approved :: MIT License",
    ],
)
