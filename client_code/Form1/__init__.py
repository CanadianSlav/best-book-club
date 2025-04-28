from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Form1(Form1Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.

    def favourite_books_button_click(self, **event_args):
        """This method is called when the button is clicked"""
        pass

    def add_article_button_click(self, **event_args):
        """This method is called when the button is clicked"""
        pass

    def login_button_click(self, **event_args):
        anvil.users.login_with_form()

    def button_logout_click(self, **event_args):
        anvil.users.logout()
        open_form('Form1')
