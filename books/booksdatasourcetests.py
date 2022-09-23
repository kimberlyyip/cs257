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
  
    def search_author_multiple_lastname(self):
	authors = self.data_source.authors('Brontë')
	self.assertTrue(len(authors) == 3)
	self.assertTrue(authors[0] == Author('Brontë', 'Ann'))
	self.assertTrue(authors[1] == Author('Brontë', 'Charolette'))
	self.assertTrue(authors[2] == Author('Brontë', 'Emily'))

    def search_author_lastname_DNE(self):
	authors = self.data_source.authors('Yip')
	self.assertTrue(len(authors) == 0)

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
	titles = self.data_source.books('\"There, There"\')
	self.assertTrue(len(titles) == 1)
	self.assertTrue(titles[0] == Book('\"There, There"\'))

    def search_title_multiple(self):
	titles = self.data_source.books('and')
	self.assertTrue(len(books) == 7)
        self.assertTrue(titles[0] == Book('And Then There Were None'))
        self.assertTrue(titles[1] == Book('Boys and Sex'))
        self.assertTrue(titles[2] == Book('Girls and Sex'))
        self.assertTrue(titles[3] == Book('Hard-Boiled Wonderland and the End of the World'))
        self.assertTrue(titles[4] == Book('Pride and Prejudice'))
        self.assertTrue(titles[5] == Book('Sense and Sensibility'))
        self.assertTrue(titles[6] == Book('\"The Life and Opinions of Tristram Shandy, Gentleman\"'))

    def sort_author(self):
	authors_list = self.data_source.authors()
	self.assertTrue(len(authors_list) == 4))
	self.assertTrue(authors_list[0] == Author('Austen', 'Jane'))
	self.assertTrue(authors_list[1] == Author('Brontë', 'Ann')) 
	self.assertTrue(authors_list[2] == Author('Brontë', 'Charlotte')) 
	self.assertTrue(authors_list[3] == Author('Brontë', 'Emily'))




if __name__ == '__main__':
    unittest.main()

