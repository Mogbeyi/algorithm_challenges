class CountFrequency:

    def __init__(self, arr):
        self.arr = arr
        self.freq_arr = [0] * 100

    def get_freq(self):
        for num in self.arr:
            self.freq_arr[num] += 1

        return self.freq_arr

class Sort:

    def __init__(self, freq):
        self.arr = freq.get_freq()
        self.result = []

    def sort_data(self):
        for i in range(100):
            for val in range(self.arr[i]):
                if self.arr[i] != 0:
                    self.result.append(i)

        return self.result

def main():
    b = CountFrequency([3,3,3,5,5,5,99,99,99,89,89,78,78])
    a = Sort(b)
    print(a.sort_data())

main()


