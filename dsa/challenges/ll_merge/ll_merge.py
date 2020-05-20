class LinkedList:
    def __init__(self, value=None):
        self.head = None

    def __str__(self):
        output = ""
        current = self.head
        while current:
            output += f"{{ {str(current.value)} }} -> "
            current = current.next
        return output + "NULL"

    def __repr__(self):
        return f"LinkedList: {self.head}"

    def insert(self, value):
        """Function creates a new node and adds it to the head of the linked list"""
        self.head = Node(value, self.head)

    def insertBefore(self, value, newVal):
        """Function has two parameters a value: inside the linked list and newVal: item to be added. This will create a new node with the newVal and insert it before the given value"""
        current = self.head

        while current:
            if current.next == None:
                return "Value not found."
            if current.next.value == value:
                current.next = Node(newVal, current.next)
                break
            current = current.next

    def insertAfter(self, value, newVal):
        """Function has two parameters a value: inside the linked list and newVal: item to be added. This will create a new node with the newVal and insert it after the given value"""
        if self.head == None:
            self.head = Node(value, self.head)
        else:
            current = self.head

            while current:
                if current.next == None:
                    raise ValueError("Value not found.")
                if current.value == value:
                    current.next = Node(newVal, current.next)
                    break
                current = current.next

    def includes(self, value):
        """Returns whether or not a value is within the linked list. Boolean output"""
        current = self.head

        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def append(self, value, next_=None):
        """Function creates a new node and appends it to the tail of the linked list"""
        if self.head == None:
            self.head = Node(value, self.head)
        else:
            current = self.head

            while current:
                if current.next == None:
                    current.next = Node(value, next_)
                    break
                current = current.next

    def kth_from_end(self, k):
        """Returns the value of a node that is k value from the end. Parameter k is an positive integer"""
        if k < 0:
            raise ValueError("Positive integer required")

        current = self.head
        arr = []
        while current:
            arr.append(current)
            current = current.next

        if len(arr) < k:
            raise IndexError("Value extends length of List.")

        arr.reverse()

        if k == len(arr):
            k = k - 1
        return arr[k].value


class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_

        if not isinstance(next_, Node) and next_ != None:
            raise TypeError("Next must be a Node")

    def __repr__(self):
        return f"{self.value} : {self.next}"


# Note: The above code could have beeen imported to make this file a single function for the merge. I did choose to just bring it all over to keep this code challenge independent


def merge_list(list1, list2):
    """Takes two required parameters: Where list1 and list2 are both linked lists. This will merge both lists together by zipping them together. Starting with list1 head then list2, back and forth until completion. Returns a single zipped linked list."""
    if list1.head == None:
        return list2
    elif list2.head == None:
        return list1

    new_list = LinkedList()
    current1 = list1.head
    current2 = list2.head

    while current1 or current2:
        if current1:
            if new_list.head == None:
                new_list.insert(current1.value)
            else:
                new_list.append(current1.value)

        if current2:
            if new_list.head == None:
                new_list.insert(current2.value)
            else:
                new_list.append(current2.value)

        if current1 and current1.next:
            current1 = current1.next
        else:
            current1 = False

        if current2 and current2.next:
            current2 = current2.next
        else:
            current2 = False

    return new_list
