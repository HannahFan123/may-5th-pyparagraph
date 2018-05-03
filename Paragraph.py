"""Approximate Word Count
Approximate Sentence Count
Average Letter Count
Average Sentence Length"""


import os
import re
import numpy

filepath = "input.txt"


paragraph = open(filepath).read()
words = paragraph.split(" ")
#word_count = len(paragraph.split(" "))
sentence_count = len(re.split("(?<=[.!?]) +", paragraph))
letter_count = numpy.mean([len(x) for x in words])
sentence_length = words/sentence_count

print(word_count)
print(sentence_count)
print(sentence_length)
print(letter_count)



# Grab the filename from the original path







