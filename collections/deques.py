"""deques are a double-ended queue with fast appends and pops on either end"""
from collections import deque

def is_palindrome(word):
    """Return true if the given word is a palindrome"""
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True

word1 = "racecar"
word2 = "alphabet"
print(f"{word1} is a palindrome? {is_palindrome(word1)}")
print(f"{word2} is a palindrome? {is_palindrome(word2)}")
