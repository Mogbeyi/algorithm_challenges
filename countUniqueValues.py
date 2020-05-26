class UniqueValues(object):

    def __init__(self, arr):
        self.arr = arr

    def count_values(self):

        if len(self.arr) == 0:
            return 0

        if len(self.arr) == 1:
            return 1

        current_value = self.arr[0]
        unique_values = 1

        for i in range(1, len(self.arr)):
            if self.arr[i] != current_value:
                unique_values += 1
                current_value =self.arr[i]
        return unique_values


def test():
    unique = UniqueValues([1,1,1,1,1,2])
    print(unique.count_values())

test()
