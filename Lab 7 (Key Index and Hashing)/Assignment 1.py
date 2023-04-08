class KeyIndex:
    def __init__(self, array):
        max = array[0]
        min = array[0]
        # self.array=array
        for i in array:
            if i < min:
                min = i
            if i > max:
                max = i
        self.min = min
        if min < 0:
            self.new_array = [0] * (max + (min * -1) + 1)
            for i in array:
                self.new_array[i + (self.min * -1)] += 1

        else:
            self.new_array = [0] * (max + 1)
            for i in array:
                self.new_array[i] += 1

    def search(self, int_value):
        if int_value>len(self.new_array)-1:
            return False
        if self.min < 0:
            if self.new_array[int_value + (self.min * (-1))] > 0:
                return True
            return False
        else:
            if self.new_array[int_value] > 0:
                return True
            return False

    def sort(self):
        length = 0
        for i in self.new_array:
            if i > 0:
                length += (1 * i)
        self.sorted_array = [0] * length

        a = 0
        for i in range(len(self.new_array)):
            if self.new_array[i] > 0:
                for j in range(self.new_array[i]):
                    if self.min < 0:
                        self.sorted_array[a] = i + self.min
                    else:

                        self.sorted_array[a] = i
                    a += 1
        return self.sorted_array


class TestKeyIndex:
    def test_search(self):
        arr = [1, 2, -5, 4, 4, 5, 6, 7, 7, -2, -3]
        ki = KeyIndex(arr)
        return ki.search(-5)

    def test_sort(self):
        arr = [1, 2, -5, 4, 4, 5, 6, 7, 7, -2, -3]
        ki = KeyIndex(arr)
        sorted=[-5,-3,-2,1,2,4,4,5,6,7,7]
        if sorted==ki.sort():
            return True
        return False

    def run_tests(self):
        if self.test_search() and self.test_sort():
            print("All tests pass.")
a=TestKeyIndex()
a.run_tests()



