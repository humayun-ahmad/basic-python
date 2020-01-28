# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 21:56:14 2019

@author: Rajib
"""
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

#update existing entry
dict['Age'] = 8 
#Add new entry
dict['School'] = 'DPS School'

print(dict)

#remove entry with key 'Name'
del dict['Name']
print(dict)

#remove all entries in dict
dict.clear()
print(dict)

#delete entire dictionary
del dict
print(dict)


