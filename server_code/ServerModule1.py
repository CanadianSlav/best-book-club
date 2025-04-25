import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def get_books():
    return app_tables.books.search()

@anvil.server.callable
def add_review(book, rating, review_text):
    user = anvil.users.get_user()
    if user and book and rating:
        app_tables.reviews.add_row(
            user=user,
            book=book,
            rating=str(rating),
            review_text=review_text)

@anvil.server.callable
def get_reviews_for_book(book):
    return app_tables.reviews.search(book=book)
  
@anvil.server.callable
def is_favourite(book):
    user = anvil.users.get_user()
    if user:
        result = app_tables.favourites.search(user=user, book=book)
        return len(list(result)) > 0
    return False

@anvil.server.callable
def add_to_favourites(book):
    user = anvil.users.get_user()
    app_tables.favourites.add_row(user=user, book=book)

@anvil.server.callable
def get_favourites():
    user = anvil.users.get_user()
    row = app_tables.favourites.get(user=user)
    books = []
    print(row['book'])
    for item in row['book']:
        books.append(item)
        print(item)
    return books

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
