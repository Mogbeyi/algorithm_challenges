from collections import Counter

def solution(A):
    elements_frequency = Counter(A).count_frequency() 

    for elem in A:
        if elements_frequency[elem] % 2 != 0:
            return elem

class Counter(object):

    def __init__(self, array):
        self.array = array

    def count_frequency(self):
        freq_counter = {}

        for elem in self.array:
            if elem in freq_counter:
                freq_counter[elem] += 1
            else:
                freq_counter[elem] = 1

        return freq_counter


print(solution([9, 3, 9, 3, 9, 7, 9]))
