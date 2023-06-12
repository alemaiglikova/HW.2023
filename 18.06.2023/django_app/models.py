from django.db import models



class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()

class Category(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    publication_date = models.DateField()

class Rating(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()


























# import sqlite3
#
#
# conn = sqlite3.connect('books.db')
# cursor = conn.cursor()
#
#
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS User (
#         user_id INTEGER PRIMARY KEY,
#         username TEXT,
#         email TEXT,
#         password TEXT
#     )
# ''')
#
#
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS Author (
#         author_id INTEGER PRIMARY KEY,
#         name TEXT,
#         biography TEXT
#     )
# ''')
#
#
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS Category (
#         category_id INTEGER PRIMARY KEY,
#         name TEXT
#     )
# ''')
#
#
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS Book (
#         book_id INTEGER PRIMARY KEY,
#         title TEXT,
#         description TEXT,
#         author_id INTEGER,
#         category_id INTEGER,
#         publication_date DATE,
#         FOREIGN KEY (author_id) REFERENCES Author(author_id),
#         FOREIGN KEY (category_id) REFERENCES Category(category_id)
#     )
# ''')
#
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS Rating (
#         rating_id INTEGER PRIMARY KEY,
#         book_id INTEGER,
#         user_id INTEGER,
#         rating INTEGER,
#         FOREIGN KEY (book_id) REFERENCES Book(book_id),
#         FOREIGN KEY (user_id) REFERENCES User(user_id)
#     )
# ''')
#
#
# conn.close()
#
