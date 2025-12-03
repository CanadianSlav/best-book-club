from ._anvil_designer import BookListFormTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class BookListForm(BookListFormTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.repeating_panel_books.items = anvil.server.call('get_books')
        # Any code you write here will run before the form opens.
        
    def button_all_books_click(self, **event_args):
        open_form('BookListForm')
        
    def favourite_books_button_click(self, **event_args):
        open_form('MyFavouritesForm')
        
    def add_article_button_click(self, **event_args):
        open_form('BookForm')


    def login_button_click(self, **event_args):
        anvil.users.login_with_form()

    def button_logout_click(self, **event_args):
        anvil.users.logout()
        open_form('BookListForm')

    def about_us_button_click(self, **event_args):
        open_form('AboutUs')
