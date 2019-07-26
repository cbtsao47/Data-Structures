class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        current_index = self.get_size() - 1
        self._bubble_up(current_index)
        print(len(self.storage))

    def delete(self):
        last_index = self.get_size()-1
        self.storage[0], self.storage[last_index] = self.storage[last_index], self.storage[0]
        deleted = self.storage.pop()
        print('deleted')
        self._sift_down(0)
        return deleted

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        while index > 0:
            parent_index = (index-1) // 2
            if self.storage[index] > self.storage[parent_index]:
                self.storage[index], self.storage[parent_index] = self.storage[parent_index], self.storage[index]
            index = parent_index

    def _sift_down(self, index):
        while index <= self.get_size():
            left_children_index = 2*index+1
            right_children_index = 2*index+2

            out_of_bound = left_children_index > self.get_size(
            )-1 and right_children_index > self.get_size()-1 or right_children_index > self.get_size()-1 and left_children_index <= self.get_size() - 1

            if out_of_bound:
                break
            if self.storage[left_children_index] < self.storage[right_children_index]:
                if self.storage[index] < self.storage[right_children_index]:
                    self.storage[index], self.storage[right_children_index] = self.storage[right_children_index], self.storage[index]
                    index = right_children_index
            else:
                self.storage[index], self.storage[left_children_index] = self.storage[left_children_index], self.storage[index]
                index = left_children_index
    # def _sift_down(self, index):
    #     # keep going down until it's at the edge
    #     # compare parent with children]
    #     current_index = index
    #     if not self.storage[current_index]:
    #         return
    #     left_children_index = 2*current_index+1
    #     right_children_index = 2*current_index+2

    #     if left_children_index <= len(self.storage)-1 and self.storage[current_index] < self.storage[left_children_index]:
    #         self.storage[current_index], self.storage[left_children_index] = self.storage[left_children_index], self.storage[current_index]
    #         current_index = left_children_index
    #     if right_children_index <= len(self.storage)-1 and self.storage[current_index] < self.storage[right_children_index]:
    #         self.storage[current_index], self.storage[right_children_index] = self.storage[right_children_index], self.storage[current_index]
    #         current_index = right_children_index
    #     self._sift_down(current_index)
