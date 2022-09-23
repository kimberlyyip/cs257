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
	authors = self.data_source.authors("morRRiSoN")
	self.assertTrue(len(authors) == 1)
	self.assertTrue(authors[0] == Author('Morrison','Toni')) 
	
    def search_one_year(self):
	titles = self.data_source.books_between_years(2010, 2010)
	self.assertTrue(len(titles) == 1)
	self.assertTrue(titles[0] == Book('All Clear')) 
	
    def search_year_range(self):
	titles = self.data_source.books_between_years(1860, 1861)
	self.assertTrue(len(titles) == 2)
	self.assertTrue(titles[0] == Book('Great Expectations', 'Silas Marner')) 
	
    def search_year_DNE(self):
	titles = self.data_source.books_between_years(1234)
	self.assertTrue(len(titles) == 0)

    def search_title_special_char(self):
	titles = self.data_source.books('"There, There"')
	self.assertTrue(len(titles) == 1)
	self.assertTrue(titles[0] == Book('"There, There"')

    def sort_author(self):
	authors_list = self.data_source.authors()
	self.assertTrue(len(authors) == 4)
	self.assertTrue(authors[0] == Author('Austen', 'Jane')  
	self.assertTrue(authors[1] == Author('Brontë', 'Ann') 
	self.assertTrue(authors[2] == Author('Brontë', 'Charlotte') 
	self.assertTrue(authors[3] == Author('Brontë', 'Emily')




if __name__ == '__main__':
    unittest.main()

