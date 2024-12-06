"""dispatches and total orderings are great for extending functionality"""
from functools import singledispatch, singledispatchmethod, total_ordering


@singledispatch
def handle_error(error):
    raise NotImplemented("Can't handle this error type.")


@handle_error.register(TypeError)
def _(error):
    print("Handling TypeError")
    print(error)


@handle_error.register(ValueError)
def _(error):
    print("Handling ValueError")
    print(error)


@handle_error.register(ZeroDivisionError)
def _(error):
    print("Handling ZeroDivisionError")
    print(error)


class MyNum:
    def __init__(self, num):
        self.num = num

    @singledispatchmethod
    def add_it(self, another):
        raise NotImplemented("Can't add these two things!")

    @add_it.register(int)
    def _(self, another):
        self.num += another

    @add_it.register(str)
    def _(self, another):
        self.num += int(another)

    @add_it.register(list)
    def _(self, another):
        for item in another:
            self.add_it(item)


@total_ordering
class BadInt:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if isinstance(other, int | BadInt):
            return len(str(self.value)) == len(str(other))
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, int | BadInt):
            return len(str(self.value)) < len(str(other))
        return NotImplemented


if __name__ == "__main__":
    print("===== Testing singledispatch =====")
    try:
        1 + "1"
    except Exception as e:
        handle_error(e)

    try:
        int("a")
    except Exception as e:
        handle_error(e)

    try:
        1 / 0
    except Exception as e:
        handle_error(e)

    print("===== Testing singledispatchmethod =====")

    the_num = MyNum(5)
    print(the_num.num)
    the_num.add_it(13)
    print(the_num.num)
    the_num.add_it("7")
    print(the_num.num)
    the_num.add_it([1, "2", 3])
    print(the_num.num)
