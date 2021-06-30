from random import shuffle
import time


class HeapSort:

    def __init__(self, data):
        """

        :param data:
        """
        self.data = data

    def heap_sort(self):
        """
        :return:
        """
        sort_data = list()
        for i in range(len(self.data) - 1, -1, -1):
            for j in range((i + 1)//2 - 1, -1, -1):
                while j * 2 + 1 <= i:
                    if j * 2 + 2 <= i:
                        max_child = j * 2 + 1 if self.data[j * 2 + 1] < self.data[j * 2 + 2] else j * 2 + 2
                    else:
                        max_child = j * 2 + 1
                    if self.data[j] > self.data[max_child]:
                        self.data[j], self.data[max_child] = self.data[max_child], self.data[j]
                        j = max_child
                    else:
                        break
            sort_data.append(self.data[0])
            self.data[0], self.data[-1] = self.data[-1], self.data[0]
            del self.data[-1]
        return sort_data


if __name__ == "__main__":
    data = [i for i in range(25)]
    shuffle(data)
    print(data)
    start = time.time()
    data = HeapSort(data).heap_sort()
    end = time.time()
    print(data)
    print("运行时间：", end - start)

