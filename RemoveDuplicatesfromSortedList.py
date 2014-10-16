class Solution:
    def deleteDuplicates(self, head):
        if head == None:
            return head
        ptr = head
        n = ptr.next
        while n != None:
            if n.val != ptr.val:
                ptr.next = n
                ptr = n
            n = n.next
        ptr.next = None
        return head

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def main():
    head = ListNode(1)
    h = head
    h.next = ListNode(1)
    h = h.next
    h.next = ListNode(2)
    h = h.next
    h.next = ListNode(3)
    h = h.next
    h.next = ListNode(3)
    h = h.next
    h.next = ListNode(4)
    h = h.next
    h.next = ListNode(5)
    h = h.next
    h.next = ListNode(5)
    h = h.next
    h.next = ListNode(5)
    test = Solution()
    test.deleteDuplicates(head)
    h = head
    while h != None:
        print h.val
        h = h.next

if __name__ == "__main__":
    main()
