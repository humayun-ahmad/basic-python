# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 19:44:39 2019

@author: C.S.C
"""

from math import *

#print(eval('dir()', {}))
print(eval('dir()', {'sqrt': sqrt, 'pow': pow}))

print(eval('squareRoot(9)', {'squareRoot': sqrt, 'pow': pow}))
