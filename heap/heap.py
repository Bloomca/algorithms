class Heap:
    """
    Heap data structure with two operations:
    Insert in O(n * log(n))
    Extract-min (Extract-max) in O(n * log(n))

    Both types of heaps are supported, both min and max extraction
    
    Data is stored in array, with binary layers
    """
    def __init__(self, type = 'min'):
        self.data = []
        self.type = type

    """
    Parent index is always twice closer to the beginning of the array
    """
    def get_parent(self, i):
        return (i + 1) / 2 - 1

    def check_heap_property(self, parent_elem, child_elem):
        if self.type == 'min':
            return parent_elem <= child_elem
        else:
            return parent_elem >= child_elem

    """
    Insert strategy is that we add the child to the end of the array
    And then we check whether we violated or not heap structure
    Because layers are structured as binary tree, we have maximum
    log(n) layers, and in the worst case we have to replace
    elements log(n) times
    """
    def insert(self, element):
        self.data.append(element)

        child_index = len(self.data) - 1
        while child_index > 0:
            parent_index = self.get_parent(child_index)
            child_elem = self.data[child_index]
            parent_elem = self.data[parent_index]

            heap_property = self.check_heap_property(parent_elem, child_elem)
            if heap_property == False:
                self.data[parent_index] = element
                self.data[child_index] = parent_elem
                child_index = parent_index
            else:
                break

        return self.data
    
    def extract(self):
        elem = self.data[0]
        self.data[0] = self.data[-1]
        self.data = self.data[:-1]

        index = 0
        min_index = 0
        min_child = 0
        while True:
            parent_elem = self.data[index]
            children_index = index * 2
            child_left_index = children_index + 1
            child_right_index = children_index + 2

            try:
                child_left = self.data[child_left_index]
            except:
                child_left = None

            try:
                child_right = self.data[child_right_index]
            except:
                child_right = None

            if child_left is None and child_right is None:
                break;
            elif child_left is None:
                min_child = child_right
                min_index = child_right_index
            elif child_right is None:
                min_child = child_left
                min_index = child_left_index
            elif (self.type == 'min' and child_left <= child_right) or (self.type == 'max' and child_left >= child_right):
                min_child = child_left
                min_index = child_left_index
            elif (self.type == 'min' and child_left > child_right) or (self.type == 'max' and child_left < child_right):
                min_child = child_right
                min_index = child_right_index

            heap_property = self.check_heap_property(parent_elem, min_child)
            if heap_property == False:
                self.data[index] = min_child
                self.data[min_index] = parent_elem
                index = min_index
            else:
                break

        return (elem, self.data)

    def get_data(self):
        return self.data

    def get_length(self):
        return len(self.data)