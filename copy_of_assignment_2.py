# -*- coding: utf-8 -*-
"""Copy of Assignment 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17TyfRN7q0UhAbbVkzM6Nqi-6AETuggE3

Welcome to your second Assignment! Consider this as a worksheet that you will work your way there. There will be times that you need to write some code in the provided area, or explain some code that is already there. Each problem will have a description of what you need to do!

1. Loop through number 1-10, print out each number
"""

for i in range(1, 11):
  print(i)

"""2. Create a variable for an integer. Loop through numbers 1-10. Add each number in the loop to the first variable."""

for i in range(1, 11):
  print(1 + i)

"""3. Create a variable for an integer. Loop through numbers 1-10. Mulitple each number in the loop to the first variable."""

for i in range(1, 11):
  print(1 * i)

"""4. Loop through numbers 1-100. Print every number. If the number is even print out the number, even. for example: 


1

2 even

3

4 even

5
"""

for num in range(1, 101):
    if num % 2 == 0: print(num,"even")
    else: print(num)

"""Well done! You finished your second worksheet assignment from Google Coloborative. Select File -> Download .py. Take the file that you just downloaded and upload it to Canvas under Assignment 2 along with the example program in the book. If you would like you can create a link and just turn in the link by selecting Share in the top right then "Get shareable link" Copy the link and add that to your assignment in canvas."""