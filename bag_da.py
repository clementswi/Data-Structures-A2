from dynamic_array import *

class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self._da.length()) + " elements. ["
        out += ', '.join([str(self._da.get_at_index(_))
                          for _ in range(self._da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.length()

    # -----------------------------------------------------------------------

    def add(self, value: object) -> None: #passes the prescribed test
        """
        Add a new element to the bag.
        This method is implemented with O(1) amortized runtime complexity.
        """
        self._da.append(value)

    def remove(self, value: object) -> bool: #passes the prescribed test
        """Remove an element from the bag that matches the provided value object.
                Returns True if an object was removed, otherwise, returns False.
                This method is implemented with O(N) runtime complexity.
                """
        for i in range(self._da.length()):
            if self._da.get_at_index(i) == value:
                self._da.remove_at_index(i)
                return True
        return False

    def count(self, value: object) -> int: #passes the prescribed test
        """
                Return the number of elements in the bag that match the provided value object.
                This method is implemented with O(N) runtime complexity.
                """
        count = 0
        for i in range(self._da.length()):
            if self._da.get_at_index(i) == value:
                count += 1
        return count

    def clear(self) -> None: #passes the prescribed test
        """Clear the contents of the bag. This method is implemented with O(1) runtime complexity.
                """
        self._da = DynamicArray()

    def equal(self, second_bag: "Bag") -> bool:
        if self.size() != second_bag.size():
            return False

        # Create a DynamicArray to store the elements in the first bag
        value_counts = DynamicArray()
        for i in range(self.size()):
            value_counts.append(self._da.get_at_index(i))

        # Check if the second bag has the same number of occurrences for each value
        for i in range(second_bag.size()):
            value = second_bag._da.get_at_index(i)
            found = False
            for j in range(value_counts.length()):
                if value == value_counts.get_at_index(j):
                    value_counts.remove_at_index(j)
                    found = True
                    break
            if not found:
                return False

        return True

    def __iter__(self): #passed the prescribed test
        self._iterator_index = 0  # Reset the iterator index when starting a new iteration
        return self

    def __next__(self): #passed the prescribed test
        if self._iterator_index < self._da.length():
            item = self._da.get_at_index(self._iterator_index)
            self._iterator_index += 1
            return item
        else:
            raise StopIteration