"""Counters are a type of dictionary that stores how many of each object is encountered"""
from io import BytesIO
import tokenize
from collections import Counter
from pathlib import Path

source = Path(__file__).read_bytes()
# Tokenize the source code
tokens = tokenize.tokenize(BytesIO(source).readline)
# Filter out any non-NAME tokens
tokens = [token.string.lower() for token in tokens if token.type == tokenize.NAME]
# Create a Counter of the identifiers
token_counter = Counter(tokens)
# Print the total number of tokens
print(token_counter.total())
# Print the 5 most common tokens
print(token_counter.most_common(5))
# Print the 3 least common tokens
print(token_counter.most_common()[:-4:-1])
