from ._anvil_designer import MyFavouritesFormTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class MyFavouritesForm(MyFavouritesFormTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
    
        user = anvil.users.get_user()
        if not user:
            alert("You must be logged in to view your favorite books.")
            open_form('BookListForm')  # Send them back to book list
            return
    
        no_favourites = anvil.server.call('no_favourites')
        
        if no_favourites:
            alert("You must favourite a book first.")
            open_form('BookListForm')  # Send them back to book list
            return

        self.repeating_panel_favourites.items = anvil.server.call('get_favorite_books')
        
        # Any code you write here will run before the form opens.

      

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
