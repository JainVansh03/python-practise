class MergeSort:
    def __init__(self, data):
        self.data = data

    def sort(self):
        self.data = self._merge_sort(self.data)
        return self.data

    def _merge_sort(self, array):
        if len(array) <= 1:
            return array

        mid = len(array) // 2
        left_half = self._merge_sort(array[:mid])
        right_half = self._merge_sort(array[mid:])

        return self._merge(left_half, right_half)

    def _merge(self, left, right):
        merged = []
        left_index = right_index = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1

        # Append any remaining elements
        merged.extend(left[left_index:])
        merged.extend(right[right_index:])

        return merged

a = []
print("Enter the size of list:")
b = int(input())
print("Enter the element:")
for i in range(b):
    a.append(int(input()))

mergesort = MergeSort(a)
sorted_data = mergesort.sort()
print("Sorted Array:", sorted_data)
    