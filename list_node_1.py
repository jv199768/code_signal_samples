class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value     # Holds the value or data of the node
        self.next = next       # Points to the next node in the linked list; default is None

# Initialization of linked list
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
