from main_4 import VirtualLibrary


def test_add_book():
  library = VirtualLibrary()
  library.add_book("Vinte mil léguas submarinas")
  assert "Vinte mil léguas submarinas" in library.list_book()


def test_remove_book():
  library = VirtualLibrary()
  library.add_book("Laranja Mecânica")
  library.remove_book("Laranja Mecânica")
  assert "Laranja Mecânica" not in library.list_book()


def test_list_books():
  library = VirtualLibrary()
  library.add_book("1984")
  library.add_book("Eu, Robô")
  assert library.list_book() == ["1984", "Eu, Robô"]
