import pandas as pd
import numpy as np

class BookLover():
    '''This class organizes a book lover's content such as books they've read, favorite books, book ratings, and favorite genre 
    as well as storing their name and email'''
    def __init__(self, name: str, email: str, fav_genre: str, num_books: int = 0, book_list: pd.DataFrame = pd.DataFrame({'book_name':[], 'book_rating':[]})):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list
        
    def add_book(self, book_name: str, book_rating: int):
        if isinstance(book_rating, int) and book_rating >= 0 and book_rating <= 5:
            if self.book_list.empty or book_name not in self.book_list['book_name'].values:
                new_book = pd.DataFrame({
                'book_name': [book_name],
                'book_rating': [book_rating]
                })
                self.book_list = pd.concat([self.book_list, new_book], ignore_index = True)
                return
            else:
                print('Sorry, cannot add. Book name already exists.')
        else:
            print('Invalid input. Rating must be integer ranging 0 to 5.')
        
    def has_read(self, book_name):
        if book_name in self.book_list['book_name'].values:
            return True
        else:
            return False
    
    def num_books_read(self):
        return len(self.book_list)
    
    def fav_books(self):
        return self.book_list[self.book_list['book_rating'] > 3]
