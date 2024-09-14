from typing import List


class Vector:
    def __init__(self, initial_len: int = 5, factor: int = 2):
        self._arr: List[int] = [None] * initial_len
        self._size = 0
        self._factor = factor

    def append(self, num: int) -> None:
        # Create a new arr with length multiplied by factor
        if self._size == len(self._arr):
            new_arr = [None] * (self._size * self._factor)

            # Copy current arr into the new one
            for i in range(self._size):
                new_arr[i] = self._arr[i]

            # Override the current arr with the new one
            self._arr = new_arr

        # Adding the new num into the current arr
        self._arr[self._size] = num
        self._size += 1

    def __str__(self):
        return str(self._arr[:self._size])


# Create a Vector instance
v = Vector(initial_len=10, factor=3)

# Append elements
v.append(1)
v.append(2)
v.append(3)
v.append(4)
v.append(5)
v.append(6)
v.append(7)
v.append(8)
v.append(9)
v.append(10)
v.append(11)

# Print the Vector
print(v)
