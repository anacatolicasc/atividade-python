import pytest


class VirtualLibrary:

  def __init__(self):
    self.books = []

  def add_book(self, titulo):
    self.books.append(titulo)

  def remove_book(self, titulo):
    if titulo in self.books:
      self.books.remove(titulo)

  def list_book(self):
    return self.books
