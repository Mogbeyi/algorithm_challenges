import unittest
import re


class WordCloudData(object):
    def __init__(self, input_string):
        self.words_to_counts = {}
        self.input_string = input_string
        self.split_string = self.input_string.lower().split()

    def count_words(self):
        for char in self.split_string:
            char = re.sub(r"[^\w\s]", "", char)
            if len(char) == 1 and char.isalpha == False:
                continue
            if char in self.words_to_counts:
                self.words_to_counts[char] += 1
            else:
                self.words_to_counts[char] = 1

        return self.words_to_counts

    def print_result(self):
        print(self.count_words())


first = WordCloudData("I like cake")
first.print_result()
second = WordCloudData("Dessert - mille-feuille cake")
second.print_result()
third = WordCloudData("Allie's Bakery: Sasha's... Cakes")
third.print_result()
