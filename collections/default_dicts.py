"""defaultdict is great for simplifying nested dictionary structures"""
from collections import defaultdict

word_list = ["orange", "apple", "watermelon", "apple", "watermelon", "grape", "apple"]

counter = defaultdict(int)
for word in word_list:
    counter[word] += 1

print(counter)

def infinite_dict():
    return defaultdict(infinite_dict)

infidict = infinite_dict()
infidict["first"]["second"]["third"]["fourth"] = 42
