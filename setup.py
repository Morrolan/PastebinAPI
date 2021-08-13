#!/usr/bin/env python

#############################################################################
#    Pastebin.py - Python Pastebin API.
#    Copyright (C) 2012 - 2019 Ian Havelock
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

#############################################################################

# This software is a derivative work of:
# http://winappdbg.sourceforge.net/blog/pastebin.py

#############################################################################

from setuptools import setup

long_desc = open('readme.rst').read()
install_requires = open('requirements.txt').read().split('\n')

setup(name='Pastebin',
      version='2.0',
      py_modules=['pastebin'],
      author='Ian Havelock',
      author_email='ian@morrolan.com',
      url='http://www.morrolan.com',
      license='GNU General Public License (GPL)',
      description='Python Pastebin API interaction object.',
      long_description=long_desc,
      platforms=['Windows', 'Unix', 'OS X'],
      download_url="http://pypi.python.org/pypi/Pastebin/",
      keywords=["pastebin", "paste", "xml", "pastebin API"],
      classifiers=[
          "Programming Language :: Python",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Development Status :: 5 - Production/Stable",
          "Environment :: Other Environment",
          "Intended Audience :: Developers",
          "Intended Audience :: Education",
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Operating System :: OS Independent",
          "Topic :: Education",
          "Topic :: Internet",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      install_requires=install_requires,

      )
