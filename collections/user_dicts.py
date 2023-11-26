"""User* classes are a good way to create custom versions of their builtins"""
from collections import UserDict

class Box(UserDict):
    def __getattr__(self, key):
        # Allow attribute access for dictionary keys
        if key in self.data:
            return self.data[key]
        else:
            raise AttributeError(f"'Box' object has no attribute '{key}'")

    def __setattr__(self, key, value):
        # Allow setting attributes for dictionary keys
        if key == 'data':
            super().__setattr__(key, value)
        else:
            self.data[key] = value

    def __delattr__(self, key):
        # Allow deleting attributes for dictionary keys
        if key in self.data:
            del self.data[key]
        else:
            raise AttributeError(f"'Box' object has no attribute '{key}'")

# Example usage
# Define a dictionary for a Star Trek character
character = Box({'name': 'Spock', 'species': 'Vulcan', 'rank': 'Commander'})

# Accessing entries using dotted attribute access
print(character.name)  # Output: Spock
print(character.species)  # Output: Vulcan
print(character.rank)  # Output: Commander

# Modifying entries using dotted attribute access
character.rank = 'Captain'
print(character.rank)  # Output: Captain

# Deleting entries using dotted attribute access
del character.rank
print(character)
