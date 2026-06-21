# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        while not head or not head.next:
            return head
        prev=head.next
        curr=head
        pre=prev
        while prev and prev.next:
            curr.next=prev.next
            curr=curr.next
            prev.next=curr.next
            prev=prev.next
        curr.next=pre
        return head