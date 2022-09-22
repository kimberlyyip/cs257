'''
   booksdatasourcetest.py
   Jeff Ondich, 24 September 2021
   Authors: Sydney Nguyen and Kimberly Yip
'''

from booksdatasource import Author, Book, BooksDataSource
import unittest

class BooksDataSourceTester(unittest.TestCase):
    def setUp(self):
        self.data_source = BooksDataSource('books1.csv')

    def tearDown(self):
        pass

    def test_unique_author(self):
        authors = self.data_source.authors('Pratchett')
        self.assertTrue(len(authors) == 1)
        self.assertTrue(authors[0] == Author('Pratchett', 'Terry'))

    def search_author_two_lastname(self):
	auhtors = self.data_source.authors('Grenville Wodehouse')
	self.assertTrue(len(authors) == 1)
	self.assertTrue(authors[0] == Author('Grenville Wodehouse', 'Pelham') 

if __name__ == '__main__':
    unittest.main()

