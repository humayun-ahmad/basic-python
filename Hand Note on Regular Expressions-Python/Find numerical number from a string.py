# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Find numerical number from regular expression or string
#find a number from a string 
import re

text = "my phone number is 01796000000"
phoneRegex = re.compile(r"\d\d\d\d\d\d\d\d\d\d\d")

print(phoneRegex.search(text))