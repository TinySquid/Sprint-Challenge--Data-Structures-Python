from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        self.oldest_item = 0

    def append(self, item):
        """When the ring buffer is full and a new element is inserted, 
        the oldest element in the ring buffer is overwritten with the 
        newest element.
        
        append method adds elements to the buffer. 
        """

        if len(self.storage) == self.capacity:
            # Overwrite
            if self.oldest_item == 0:
                self.oldest_item = self.capacity
            node_to_overwrite = self.storage.head

            for i in range(1, self.oldest_item):
                node_to_overwrite = node_to_overwrite.next

            node_to_overwrite.value = item
            self.oldest_item -= 1
        else:
            # Append
            self.storage.add_to_head(item)
            self.oldest_item += 1

    def get(self):
        """returns all of the elements in the buffer in a list in their 
        given order. 
        It should not return any None values in the list even if they are 
        present in the ring buffer.
        """
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        current_node = self.storage.tail

        while current_node:
            if current_node.value != None:
                list_buffer_contents.append(current_node.value)
            current_node = current_node.prev

        return list_buffer_contents


# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
