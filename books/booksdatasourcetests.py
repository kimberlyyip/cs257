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
	authors = self.data_source.authors('Grenville Wodehouse')
	self.assertTrue(len(authors) == 1)
	self.assertTrue(authors[0] == Author('Grenville Wodehouse', 'Pelham'))

    def search_author_special_character(self):
	authors = self.data_source.authors('García Márquez')
	self.assertTrue(len(authors) == 1)
	self.assertTrue(authors[0] == Author('García Márquez', 'Gabriel'))

    def search_author_lastname_DNE(self):
	authors = self.data_source.authors('Yip')
	self.assertTrue(len(authors) == 1)
	self.assertTrue(authors[0] == Author('')) 

    def search_case_insensitive(self):
	authors = self.data_source.books("morRRinSoN")
	self.assertTrue(len(authors) == 1)
	self.assertTrue(authors[0] == Author('Toni')) 
	
    def search_one_year(self):
	titles = self.data_source.books("2010")
	self.assertTrue(len(Book) == 1)
	self.assertTrue(titles[0] == Book('All Clear')) 
	
    def search_year_range(self):
	titles = self.data_source.books_between_years("1963"."1974")
	self.assertTrue(len(Book) == 2)
	self.assertTrue(titles[0] == Book('The Spy Who Came in From the Cold', "Tinker, Tailor, Soldier, Spy")) 
	
    def search_year_DNE(self):
	titles = self.data_source.books_between_years("1234")
	self.assertTrue(len(Book) == 1)
	self.assertTrue(titles[0] == Book("")) 




if __name__ == '__main__':
    unittest.main()

