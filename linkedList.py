"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        count = 1
        current = self.head
        if position == 1:
            return self.head
        else:
            while current and count <= position:
                if count == position:
                    return current
                current = current.next
                count += 1

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        current = self.head
        count = 1
        while current and count < position:
            if count == position-1:
                new_element.next = current.next
                current.next = new_element
            current = current.next
            count += 1

    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        count = 0
        while current.next:
            if current.value == value:
                count = 1
                if count == 1:
                    current = current.next
            else:
                current = current.next
            print current.value
            print current.next.value


# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print ll.head.next.next.value
# Should also print 3
print ll.get_position(3).value # position in LinkedList
#print ll.get_position(4).value # position not in LinkedList
print "Done get_position"
# Test insert
ll.insert(e4,3)
# Should print 4 now
print "Should print 1"
print ll.get_position(1).value
print "Should print 2"
print ll.get_position(2).value
print "Should print 4"
print ll.get_position(3).value
print "Should print 3"
print ll.get_position(4).value

# Test delete
print "Test delete"
ll.delete(1)
# Should print 2 now
print "Print 2"
print ll.get_position(1).value
# Should print 4 now
print "Print 4"
print ll.get_position(2).value
# Should print 3 now
print "Print 3"
print ll.get_position(3).value
