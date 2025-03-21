class InsertionSort:
    def __init__(self, data):
        self.data = data

    def sort(self):
        for i in range(1, len(self.data)):
            key = self.data[i]
            j = i - 1
            while j >= 0 and key < self.data[j]:
                self.data[j + 1] = self.data[j]
                j -= 1
            self.data[j + 1] = key
        return self.data

# Example usage:

a = []
print("Enter the size of list:")
b = int(input())
print("Enter the element:")
for i in range(b):
    a.append(int(input()))
insertion_sort = InsertionSort(a)
sorted_data = insertion_sort.sort()
print("Insertion Sort:", sorted_data)
