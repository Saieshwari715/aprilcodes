# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return
        curr=head
        l=0
        while curr:
            l+=1
            curr=curr.next
        temp=head
        c=0
        
        mid=l//2
        while c<mid-1:
            c+=1
            temp=temp.next
        temp.next=temp.next.next
        return head




            

        