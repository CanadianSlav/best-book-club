from ._anvil_designer import BookFormTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class BookForm(BookFormTemplate):
    def __init__(self, book=None, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        
        self.book = book
    
        # If editing an existing book, fill in the fields
        if self.book:
            self.text_box_title.text = self.book['title']
            self.text_box_author.text = self.book['author']
            self.text_box_genre.text = self.book['genre']
            self.text_area_summary.text = self.book['summary']
            # can't set file directly to FileLoader, so just leave it empty
    
    def file_loader_cover_change(self, file, **event_args):
        # You don't need to set anything here unless you want a preview
        pass
    
    def button_submit_click(self, **event_args):
        # Figure out which cover image to use
        cover_image = self.file_loader_cover_image.file
        if not cover_image and self.book:
            cover_image = self.book['cover_image']
    
        if self.book:
        # Update the existing book
            anvil.server.call('update_book',
                            book=self.book,
                            title=self.text_box_title.text,
                            author=self.text_box_author.text,
                            genre=self.text_box_genre.text,
                            summary=self.text_area_summary.text,
                            cover_image=cover_image)
        else:
        # Add a new book
            anvil.server.call('add_new_book',
                            title=self.text_box_title.text,
                            author=self.text_box_author.text,
                            genre=self.text_box_genre.text,
                            summary=self.text_area_summary.text,
                            cover_image=cover_image)
    
        # After adding/updating, go back to the book list
        open_form('BookListForm')
    
    def button_cancel_click(self, **event_args):
        open_form('BookListForm')


    def button_all_books_click(self, **event_args):
        open_form("BookListForm")

    def favourite_books_button_click(self, **event_args):
        open_form("MyFavouritesForm")

    def add_article_button_click(self, **event_args):
        open_form("BookForm")

    def login_button_click(self, **event_args):
        anvil.users.login_with_form()

    def button_logout_click(self, **event_args):
        anvil.users.logout()
        open_form("BookListForm")
