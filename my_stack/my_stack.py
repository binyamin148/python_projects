from typing import Any


class MyStack:
    """A class representing a stack data structure."""

    def __init__(self):
        """Initialize an empty stack."""
        self._items = []

    def push(self, element=None) -> bool:
        """Push an element onto the stack.

        Args:
            element: The element to be pushed onto the stack.

        Returns:
            bool: True if the element was successfully pushed, False otherwise.
        """
        if element is None:
            return False
        self._items.append(element)
        return True

    def pop(self) -> Any:
        """Remove and return the top element from the stack.

        Returns:
            Any: The top element of the stack.
        """
        if self.is_empty():
            return None
        return self._items.pop()

    def peek(self) -> Any:
        """Return the top element from the stack without removing it.

        Returns:
            Any: The top element of the stack.
        """
        if self.is_empty():
            return None
        return self._items[-1]

    def is_empty(self) -> bool:
        """Check if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return len(self._items) == 0

    def size(self) -> int:
        """Return the number of elements in the stack.

        Returns:
            int: The number of elements in the stack.
        """
        return len(self._items)

    def clear(self) -> None:
        """Remove all elements from the stack."""
        self._items.clear()

        
# Create an instance of the stack
stack = MyStack()

# Check if the stack is empty
print("Is the stack empty?", stack.is_empty())  # Expected: True

# Add elements to the stack
stack.push(5)
stack.push(10)
stack.push(15)

# Check the size of the stack
print("Stack size:", stack.size())  # Expected: 3

# Peek at the top element
print("Top element:", stack.peek())  # Expected: 15

# Remove an element from the stack
popped_item = stack.pop()
print("Popped item:", popped_item)  # Expected: 15

# Check the new size
print("Stack size after pop:", stack.size())  # Expected: 2

# Try to add None
print("Adding None:", stack.push(None))  # Expected: False

# Display the new top element
print("New top element:", stack.peek())  # Expected: 10

# Clear the stack
stack.clear()
print("Stack size after clearing:", stack.size())  # Expected: 0

# Try to pop from an empty stack
print("Attempt to pop from empty stack:", stack.pop())  # Expected: None

        
        
