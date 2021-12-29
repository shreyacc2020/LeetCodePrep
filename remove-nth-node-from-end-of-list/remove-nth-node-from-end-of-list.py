# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        ptr1 = ptr2 = head
        while(ptr1):
            ptr1 = ptr1.next
            count+=1
        index = count - n
        if count == 1:
            if n == 1:
                head = None
                return None

        elif count == 2:
            if n == 1:
                head.next = None
                return head
            elif n == 2:
                head = head.next
                return head

        elif count>2:
            if index == 0:
                head = head.next
                return head
            for i in range(0,index):
                if i == (index-1):
                    ptr2.next = ptr2.next.next
                else:
                    ptr2 = ptr2.next
            return head

        
        
        