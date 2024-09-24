class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_linked_list(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

# Example usage:
# Linked List: 1 -> 2 -> 3 -> None
head = ListNode(1, ListNode(2, ListNode(3)))
reversed_head = reverse_linked_list(head)
while reversed_head:
    print(reversed_head.value, end=" -> ")
    reversed_head = reversed_head.next
# Output: 3 -> 2 -> 1 ->
