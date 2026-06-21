# Last Updated: 6/22/2026, 12:44:17 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(-1)
        curr=head
        dummy.next=head
        prev=dummy
        while curr and curr.next:
            if curr.val==curr.next.val:
                while curr and curr.next and curr.val==curr.next.val:
                    curr=curr.next
                prev.next=curr.next
            else:
                prev=prev.next
            curr=curr.next
        return dummy.next
