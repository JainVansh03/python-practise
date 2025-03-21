class SelectionSort:
    def __init__(self, data):
        self.data = data

    def sort(self):
        for i in range(len(self.data)):
            min_idx = i
            for j in range(i + 1, len(self.data)):
                if self.data[j] < self.data[min_idx]:
                    min_idx = j
            self.data[i], self.data[min_idx] = self.data[min_idx], self.data[i]
        return self.data

# Example usage:

a = []
print("Enter the size of list:")
b = int(input())
print("Enter the element:")
for i in range(b):
    a.append(int(input()))
selection_sort = SelectionSort(a)
sorted_data = selection_sort.sort()
print("Selection Sort:", sorted_data)
