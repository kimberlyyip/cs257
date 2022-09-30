'''
    books.py
    Jeff Ondich, 21 September 2022
    For use in the "books" assignment at the beginning of Carleton's
    CS 257 Software Design class, Fall 2022.
    
    Authors: Kimberly Yip and Sydney Nguyen
'''

import csv 
import sys
import booksdatasource

def main():
  file = booksdatasource.BooksDataSource('books1.csv')
  if(len(sys.argv) == 1):
    output = file.books()
  elif("-h" or "--help" in sys.argv):
     usage = open('usage.txt')
     print(usage.read())
     usage.close()
  elif(sys.argv[1] == "authors"):
    if len(sys.argv) == 2:
      output = file.authors()
    elif len(sys.argv) == 3:
      if(sys.argv[2] == '-t'):
        output = file.authors(sys.argv[2],sys.argv[3])
    else:
      raise SyntaxError("Amount of inputs can not be handled")
  elif(sys.argv[1] == "books"):
    if len(sys.argv) == 2:
      output = file.books()
    elif len(sys.argv) == 3:
      output = file.books(sys.argv[2])
    else:
      raise SyntaxError("Amount of inputs can not be handled")
  elif(sys.argv[1] == "range"):
    if len(sys.argv) == 3:
      output = file.books_between_years()
    elif len(sys.argv) == 4:
      output = file.books_between_years(sys.argv[2])
    elif len(sys.arv) == 5:
      output = file.books_between_years(sys.argv[2],sys.argv[3])
    else:
      raise SyntaxError("Amount of inputs can not be handled")     
    print(output)
    
main()
