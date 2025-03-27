# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def GCD(self,a,b):
            while b!=0:
                temp=b
                b=a % b 
                a=temp
            return a
    
        prev=head
        cur=head.next
        while cur:
            s=GCD(self,prev.val,cur.val)
            k=ListNode(s)
            prev.next=k
            k.next=cur
            prev=cur
            cur=cur.next
        return head


        