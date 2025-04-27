from ._anvil_designer import BooksRepeatingTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class BooksRepeating(BooksRepeatingTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def details_button_click(self, **event_args):
    open_form('BookDetailForm', book=self.item)

  def edit_button_click(self, **event_args):
    open_form('BookForm', book=self.item)

  def delete_button_click(self, **event_args):
    if confirm("Are you sure you want to delete this book?"):
        anvil.server.call('delete_book', self.item)
        open_form('BookListForm')