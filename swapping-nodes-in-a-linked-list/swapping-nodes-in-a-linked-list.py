# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = []
        ptr = head
        count = 0
        while(ptr):
            arr.append(ptr.val)
            ptr = ptr.next
            count+=1
        print(arr)
        
        # nodes to be swapped are k=> (k-1) index from start and (count-k) index from start
        temp = arr[count-k]
        arr[count-k] = arr[k-1]
        arr[k-1] = temp
            
        cur = dummy = ListNode(0)
        for i in arr:
            cur.next = ListNode(i)
            cur = cur.next
        return dummy.next
            