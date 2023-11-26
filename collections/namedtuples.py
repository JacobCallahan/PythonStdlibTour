"""named tuples are a good shortcut for creating a class with only properties"""
from collections import namedtuple

Book = namedtuple("Book", ["title", "author", "year"])
bnw = Book("Brave New World", "Aldous Huxley", 1931)

print(f"{bnw.title} was written by {bnw.author} in {bnw.year}")

print(f"{bnw[0]} was written by {bnw[1]} in {bnw[2]}")

print(bnw._asdict())
