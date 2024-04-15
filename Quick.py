class QuickSort:
    def __init__(self, array):
        self.array = array

    def partition(self, low, high):
        i = (low-1)
        pivot = self.array[high]

        for j in range(low, high):
            if self.array[j] <= pivot:
                i = i+1
                self.array[i], self.array[j] = self.array[j], self.array[i]

        self.array[i+1], self.array[high] = self.array[high], self.array[i+1]
        return (i+1)

    def quick_sort(self, low, high):
        if low < high:
            pi = self.partition(low, high)
            self.quick_sort(low, pi-1)
            self.quick_sort(pi+1, high)

    def sort(self):
        n = len(self.array)
        self.quick_sort(0, n-1)
        return self.array