# Last Updated: 6/22/2026, 12:44:12 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        llist,rlist=N=ListNode(-1),ListNode(-1)
        lt,rt=llist,rlist
        temp=head
        while temp:
            if temp.val<x:
                llist.next=temp
                llist=llist.next
            else:
                rlist.next=temp
                rlist=rlist.next
            temp=temp.next
        llist.next=rt.next
        rlist.next=None
        return lt.next
