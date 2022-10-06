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
  output = ''
  if("-h" in sys.argv or "--help" in sys.argv):
     usage = open('usage.txt')
     print(usage.read())
     usage.close()
  elif(sys.argv[1] == "authors" or sys.argv[1] == "-a"):
    if len(sys.argv) == 2:
      output = file.authors()
      for item in output:
        item.print_authors()
    elif len(sys.argv) == 3:
      output = file.authors(sys.argv[2])
      for item in output:
        item.print_authors()
    else:
      raise SyntaxError("Amount of inputs can not be handled")
  elif(sys.argv[1] == "books" or sys.argv[1] == "-b"):
    if len(sys.argv) == 2:
      output = file.books()
      for item in output:
        item.print_books()
    elif len(sys.argv) == 3:
      output = file.books(sys.argv[2])
      for item in output:
        item.print_books()
    elif len(sys.argv) == 4:
      if sys.argv[3] == '-t':
        output = file.books(sys.argv[2])
        for item in output:
          item.print_books()
      elif sys.argv[3] == '-y':
        output = file.books(sys.argv[2])
        for item in output:
          year_sorted = sorted(item.books, key = lambda book: book.publication_year)
          year_sorted.print_books()
    else:
      raise SyntaxError("Amount of inputs can not be handled")
  elif(sys.argv[1] == "range" or sys.argv[1] == "-r"):
    if len(sys.argv) == 2:
      output = file.books_between_years()
      for item in output:
        item.print_books()
    elif len(sys.argv) == 3:
      output = file.books_between_years(sys.argv[2])
      for item in output:
        item.print_books()
    elif len(sys.argv) == 4:
      output = file.books_between_years(sys.argv[2],sys.argv[3])
      for item in output:
        item.print_books()
    else:
      raise SyntaxError("Amount of inputs can not be handled")     
  # for item in output:
  #   for book in item.books:
  #     print(book.title)
    
main()
