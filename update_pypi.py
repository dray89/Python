# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 14:10:49 2019

@author: rayde
"""
cd C:\Users\rayde\iCloudDrive\GitHub\finance_python
python setup.py sdist
twine upload --repository-url https://test.pypi.org/legacy/ dist/*

twine upload dist/*