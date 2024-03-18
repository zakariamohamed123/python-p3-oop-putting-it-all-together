#!/usr/bin/env python3

class Book:
   
    def _init_(self, title):
        self.title = title
        

    def get_page_count(self):
        return self.page_count
    
    def set_page_count(self, page_count):
        if (type(page_count) == int):
            self.page_count = page_count
        else:
            print("page_count must be an integer.")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    
    page_count = property(get_page_count, set_page_count)   
    
        