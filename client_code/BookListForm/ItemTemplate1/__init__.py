from ._anvil_designer import ItemTemplate1Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class ItemTemplate1(ItemTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def details_button_click(self, **event_args):
    open_form('BookDetailForm', book=self.item)

  def edit_button_click(self, **event_args):
    open_form('BookForm', book=self.item)

  def delete_button_click(self, **event_args):
    app_tables.books.delete_row(self.item)
    open_form('BookListForm')  # Refresh list