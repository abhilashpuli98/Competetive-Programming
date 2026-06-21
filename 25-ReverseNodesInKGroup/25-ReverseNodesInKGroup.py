# Last Updated: 6/22/2026, 12:45:11 AM
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def kthNode(startNode : ListNode,k : int):
            while startNode and k>0:
                startNode=startNode.next
                k-=1
            return startNode
        dummy=ListNode(0,head)
        prevgroup=dummy
        while True:
            kthnode=kthNode(prevgroup,k)
            if not kthnode:
                break
            groupNext=kthnode.next
            prev,curr=kthnode.next,prevgroup.next
            while curr!=groupNext:
                nn=curr.next
                curr.next=prev
                prev=curr
                curr=nn
            temp=prevgroup.next
            prevgroup.next=kthnode
            prevgroup=temp
        return dummy.next
            



