import heapq


class Elem:
    def __init__(self, sorted_list: list):
        self.sorted_list = sorted_list
        self.sorted_list.append(float("inf"))

    def __lt__(self, other):
        return self.sorted_list[0] < other.sorted_list[0]

    def __repr__(self):
        return f'{self.sorted_list}'

    def pop_smallest(self):
        return self.sorted_list.pop(0)


one = Elem([4, 6, 17])
two = Elem([1, 5, 9])
three = Elem([8, 10, 18])
four = Elem([2, 4, 11])

heap = [three, one, four, two]
heapq.heapify(heap)

final = []

for i in range(12):
    smallest_elem = heap[0]
    final.append(smallest_elem.pop_smallest())
    heapq.heapreplace(heap, smallest_elem)


print(final)
