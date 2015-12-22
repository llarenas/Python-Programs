#!/usr/bin/python
# coding: utf-8

"""
Written by Ronel Llarenas.


$ python array_generator.py
	Enter the array name:
	>  name

	Enter your string:
	>  array filled with the splitted string 

  Result:
	Array name
	name = ['array', 'filled', 'with', 'the', 'splitted', 'string']

"""

name = input("\nEnter the name of your array.\n>")
items = input("\nEnter your strings.\n>")
array = items.split("-")
print ("\n\nArray name: ", name)
print (name, " = ", array)
