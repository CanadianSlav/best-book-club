from ._anvil_designer import BookDetailFormTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class BookDetailForm(BookDetailFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_add_fav_click(self, **event_args):
    user = anvil.users.get_user()
    book = self.item
    existing = app_tables.favorites.search(user=user, book=book)
    if not existing:
        app_tables.favorites.add_row(user=user, book=book)
      
  def load_reviews(self):
    self.repeating_panel_reviews.items = app_tables.reviews.search(book=self.item)

  def button_submit_review_click(self, **event_args):
    app_tables.reviews.add_row(
        user=anvil.users.get_user(),
        book=self.item,
        rating=self.dropdown_rating.selected_value,
        review_text=self.text_area_review.text
    )
    self.load_reviews()  # Refresh the reviews panel
    self.text_area_review.text = ""
    self.dropdown_rating.selected_value = None
