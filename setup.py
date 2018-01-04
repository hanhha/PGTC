#!/usr/bin/env python3

from setuptools import setup
setup (name = 'pgtc',
			version = '0.1',
			py_modules=['base_visual', 'line_visual'],
      description = 'PyGame trade charts library',
      author = 'Hanh Ha',
      author_email = 'tranhanh.haminh@gmail.com',
      license = 'MIT',
			url = 'https://github.com/hanhha/PGTC',
      install_requires = [
        'numpy',
        'pygame',
      ]
    )
