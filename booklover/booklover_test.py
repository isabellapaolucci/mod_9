import numpy as np
import pandas as pd
import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
        
        
    def setUp(self):
        
        self.test_obj1 = BookLover(name = "William Denbrough", email = "wdenbrough@gmail.com", fav_genre = "horror", book_list = pd.DataFrame({'book_name':['Storm Front'],
                                                                                                                    'book_rating':[5]}))
    def test_1_add_book(self):
        ## tests if name of new book is in the book list
        self.test_obj1.add_book("It", 3)
        name = "It"
        self.assertIn(name, self.test_obj1.book_list['book_name'].values)
        
    def test_2_add_book(self):
        ## tests to see if the code prevents a duplicate entry of a book
        self.test_obj1.add_book("It", 5)
        self.test_obj1.add_book("It", 5)
        not_expected = 2
        self.assertNotEqual(self.test_obj1.book_list['book_name'].value_counts()['It'], not_expected)
        
    def test_3_has_read(self):
        ## tests if a book is in the book list
        self.test_obj1.add_book("It", 5)
        res = self.test_obj1.has_read("It")
        self.assertTrue(res)
        
    def test_4_has_read(self):
        ## tests if a book is in the book list, returns False if not
        res2 = self.test_obj1.has_read("Twilight")
        self.assertFalse(res2)
        
    def test_5_num_books_read(self):
        ## tests method counting number of books read
        self.test_obj1.add_book("The Most Dangerous Game", 5)
        self.test_obj1.add_book("The Strain", 2)
        self.test_obj1.add_book("Game of Thrones", 1)
        self.test_obj1.add_book("The Lord of the Rings", 4)
        expected = 5
        self.assertEqual(self.test_obj1.num_books_read(), expected)
        
    def test_6_fav_books(self):
        ## tests method displaying books categorized as a favorite, counts fav books
        self.test_obj1.add_book("The Most Dangerous Game", 5)
        self.test_obj1.add_book("The Strain", 2)
        self.test_obj1.add_book("Game of Thrones", 1)
        self.test_obj1.add_book("The Lord of the Rings", 4)
        fav_books = self.test_obj1.fav_books()
        expected2 = 3
        self.assertEqual(len(fav_books), expected2)
        
if __name__ == '__main__':
    unittest.main(verbosity=3)
