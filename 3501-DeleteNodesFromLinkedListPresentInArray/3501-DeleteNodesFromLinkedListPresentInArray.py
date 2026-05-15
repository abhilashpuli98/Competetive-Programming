# Last Updated: 5/15/2026, 11:10:25 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
            nums=set(nums)
            dummy=head
            prev=None
            
            while head.val in nums:
                head=head.next
            dummy = head.next
            prev = head
            while dummy:
                if dummy.val in nums:
                    prev.next=dummy.next
                    dummy=dummy.next
                else:
                    prev=prev.next
                    dummy=dummy.next
            return head
            




                