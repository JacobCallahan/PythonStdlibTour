"""Custom encoders and decoders allow you to better handle classes"""
import json


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


bnw = Book("Brave New World", "Aldous Huxley", 1931)
jp = Book("Jurassic Park", "Michael Crichton", 1990)
books = [bnw, jp]


class BookEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Book):
            return {"type": "Book", "data": obj.__dict__}
        return super().default(obj)


def book_decoder(json_dict):
    if json_dict.get("type") == "Book":
        return Book(**json_dict["data"])
    return json_dict


with open("books.json", "w") as ex_file:
    json.dump(books, ex_file, indent=4, cls=BookEncoder)

with open("books.json") as im_file:
    imported = json.load(im_file, object_hook=book_decoder)

print(imported[0].title)
print(imported[1].title)
