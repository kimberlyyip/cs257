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

def print_authors(output):
  for item in output:
    for book in item.books:
      print(book.title)

def print_books(output):
  for item in output:
    print(item.title)

def main():
  file = booksdatasource.BooksDataSource('books1.csv')
  output = ''
  if("-h" in sys.argv or "--help" in sys.argv):
     usage = open('usage.txt')
     print(usage.read())
     usage.close()
  elif(sys.argv[1] == "authors"):
    if len(sys.argv) == 2:
      output = file.authors()
      print_authors(output)
    elif len(sys.argv) == 3:
      output = file.authors(sys.argv[2])
      print_authors(output)
    elif len(sys.argv) == 4:
      if sys.argv[3] == '-t':
        output = file.authors(sys.argv[2])
        print_authors(output)
      elif sys.argv[3] == '-y':
        output = file.authors(sys.argv[2])
        for item in output:
          year_sorted = sorted(item.books, key = lambda book: book.publication_year)
          for book in year_sorted:
            print(book.title)
    else:
      raise SyntaxError("Amount of inputs can not be handled")
  elif(sys.argv[1] == "books"):
    if len(sys.argv) == 2:
      output = file.books()
      print_books(output)
    elif len(sys.argv) == 3:
      output = file.books(sys.argv[2])
      print_books(output)
    else:
      raise SyntaxError("Amount of inputs can not be handled")
  elif(sys.argv[1] == "range"):
    if len(sys.argv) == 2:
      output = file.books_between_years()
      print_books(output)
    elif len(sys.argv) == 3:
      output = file.books_between_years(sys.argv[2])
      print_books(output)
    elif len(sys.arv) == 4:
      output = file.books_between_years(sys.argv[2],sys.argv[3])
      print_books(output)
    else:
      raise SyntaxError("Amount of inputs can not be handled")     
  # for item in output:
  #   for book in item.books:
  #     print(book.title)
    
main()
