#!/usr/bin/python3
"""
This module contains the VerboseList class that extends the built-in list class
with notification messages for modification operations.
"""


class VerboseList(list):
    """
    A custom list class that prints notification messages when items are
    added or removed from the list.
    """
    
    def append(self, item):
        """
        Append an item to the list and print a notification message.
        
        Args:
            item: The item to append to the list
        """
        super().append(item)
        print(f"Added {item} to the list.")
    
    def extend(self, iterable):
        """
        Extend the list with items from an iterable and print a notification message.
        
        Args:
            iterable: An iterable containing items to add to the list
        """
        items_count = len(list(iterable))  # Convert to list to count items
        super().extend(iterable)
        print(f"Extended the list with {items_count} items.")
    
    def remove(self, item):
        """
        Remove the first occurrence of an item from the list and print a notification message.
        
        Args:
            item: The item to remove from the list
            
        Raises:
            ValueError: If the item is not found in the list
        """
        print(f"Removed {item} from the list.")
        super().remove(item)
    
    def pop(self, index=-1):
        """
        Remove and return an item at the given index and print a notification message.
        
        Args:
            index (int, optional): The index of the item to pop. Defaults to -1 (last item).
            
        Returns:
            The item that was popped from the list
            
        Raises:
            IndexError: If the list is empty or index is out of range
        """
        if len(self) == 0:
            raise IndexError("pop from empty list")
        
        # Get the item that will be popped
        item = self[index]
        print(f"Popped {item} from the list.")
        return super().pop(index)
