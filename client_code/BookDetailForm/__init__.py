from ._anvil_designer import BookDetailFormTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class BookDetailForm(BookDetailFormTemplate):
  def __init__(self, book=None, **properties):
    self.init_components(**properties)
    self.item = book  
    self.load_reviews()  
  def load_reviews(self):
    self.repeating_panel_reviews.items = anvil.server.call('get_reviews_for_book', self.item)

    # Any code you write here will run before the form opens.

  def button_add_fav_click(self, **event_args):
    user = anvil.users.get_user()
    book = self.item

    # Check if the book is already in the user's favorites using the server-side function
    if anvil.server.call('is_favourite', book):
        alert("You already added it to your favorite list")
    else:
        # Add the book to favorites if not already present
        anvil.server.call('add_to_favourites', book)
        alert("Book added to your favorites!")
      
  def button_submit_review_click(self, **event_args):
    user = anvil.users.get_user()
    if not user:
        alert("Please log in before submitting a review.")
        return
    
    anvil.server.call(
        'add_review',
        book=self.item,
        rating=self.dropdown_rating.selected_value,
        review_text=self.text_area_review.text
    )
    self.load_reviews()
    self.text_area_review.text = ""
    self.dropdown_rating.selected_value = None

  def button_back_click(self, **event_args):
    open_form('BookListForm')
