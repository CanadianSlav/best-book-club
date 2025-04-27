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

# @anvil.server.callable
# def get_favourites():
#     user = anvil.users.get_user()
#     row = app_tables.favourites.get(user=user)
#     books = []
#     print(row['book'])
#     for item in row['book']:
#         books.append(item)
#         print(item)
#     return books

@anvil.server.callable
def get_favorite_books():
    user = anvil.users.get_user()
    favs = app_tables.favourites.search(user=user)
    return [f['book'] for f in favs]

@anvil.server.callable
def add_new_book(title, author, genre, summary, cover_image):
    app_tables.books.add_row(
        title=title,
        author=author,
        genre=genre,
        summary=summary,
        cover_image=cover_image
    )

@anvil.server.callable
def update_book(book, title, author, genre, summary, cover_image):
  book.update(
    title=title,
    author=author,
    genre=genre,
    summary=summary,
    cover_image=cover_image
  )

@anvil.server.callable
def delete_book(book):
    book.delete()

@anvil.server.callable
def delete_favourite(book):
    user = anvil.users.get_user()
    favs = app_tables.favourites.get(user=user, book=book)
    if favs:
        favs.delete()