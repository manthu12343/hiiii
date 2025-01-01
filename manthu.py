# Define a node for the doubly linked list
class Node:
    def _init_(self, data):
        self.data = data  # Store data
        self.next = None  # Pointer to the next node
        self.prev = None  # Pointer to the previous node

# Define the doubly linked list
class DoublyLinkedList:
    def _init_(self):
        self.head = None  # Initialize the head of the list

    # Add a node at the end of the list
    def append(self, data):
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
            return
        temp = self.head
        while temp.next:  # Traverse to the end of the list
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    # Add a node at the beginning of the list
    def prepend(self, data):
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    # Delete a node by value
    def delete(self, data):
        temp = self.head
        if not temp:  # If the list is empty
            print("List is empty")
            return
        # If the node to delete is the head
        if temp.data == data:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            return
        # Traverse to find the node to delete
        while temp and temp.data != data:
            temp = temp.next
        if not temp:  # Data not found
            print(f"Node with value {data} not found")
            return
        if temp.next:  # If it's not the last node
            temp.next.prev = temp.prev
        if temp.prev:  # If it's not the first node
            temp.prev.next = temp.next

    # Print the list in forward direction
    def display_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    # Print the list in reverse direction
    def display_reverse(self):
        temp = self.head
        if not temp:  # If the list is empty
            print("List is empty")
            return
        # Traverse to the end of the list
        while temp.next:
            temp = temp.next
        # Print in reverse
        while temp:
            print(temp.data, end=" ")
            temp = temp.prev
        print()

# Example usage
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.prepend(5)

print("Forward display:")
dll.display_forward()

print("Reverse display:")
dll.display_reverse()

dll.delete(20)
print("After deleting 20:")
dll.display_forward()