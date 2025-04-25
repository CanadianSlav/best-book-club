from ._anvil_designer import BookListFormTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class BookListForm(BookListFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    self.repeating_panel_books.items = anvil.server.call('get_books')
    def button_add_book_click(self, **event_args):
      open_form('BookForm')

    # Any code you write here will run before the form opens.

  def button_login_click(self, **event_args):
    anvil.users.login_with_form()

  def button_logout_click(self, **event_args):
    anvil.users.logout()
    open_form('BookListForm')

  def login_button_click(self, **event_args):
    anvil.users.login_with_form()

  def favourite_books_button_click(self, **event_args):
      open_form('MyFavouritesForm')

