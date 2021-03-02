__author__ = 'weijx.cpp@gmail.com '

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        r = ListNode(0)
        re=r
        carry=0
        while(l1 or l2):
            x= l1.val if l1 else 0
            y= l2.val if l2 else 0
            s=carry+x+y
            carry=s//10
            r.next=ListNode(s%10)
            r=r.next
            if(l1!=None):l1=l1.next
            if(l2!=None):l2=l2.next
        if(carry>0):
            r.next=ListNode(1)
        return re.next
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        r = ListNode(None)
        re = r
        while(l1, l2):
            if l1 is None:
                r.next = l2
                return re.next
            if l2 is None:
                r.next = l1
                return re.next
            x = l1.val
            y = l2.val
            if(x<y):
                r.next = ListNode(x)
                r = r.next
                if(l1!=None): l1 = l1.next
            else:
                r.next = ListNode(y)
                r = r.next
                if(l2!=None): l2= l2.next
        return re.next
    def mergeTwoLists2(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(None)
        node = res
        while l1 and l2:
            if l1.val<l2.val:
                node.next,l1 = l1,l1.next
            else:
                node.next,l2 = l2,l2.next
            node = node.next
        if l1:
            node.next = l1
        else:
            node.next = l2
        return res.next
    def plusOne(self, digits: list) -> list:
        re = digits
        lasti = len(digits) - 1
        inc = 0
        for i in range(lasti , -1 ,-1):
            if i == lasti:
                sum = re[i] + 1
                if sum>9:
                    inc = 1
                else:
                    re[i] = sum

            sum = re[i] + inc
            if sum>9:
                inc = 1
            else:
                inc = 0
            re[i] = sum%10
            if inc == 1 and i == 0:
                re.insert(0,1)
        return re
if __name__ == '__main__':
    # l12 = ListNode(3)
    # l11 = ListNode(4,l12)
    # l1 = ListNode(6,l11)
    #
    #
    # l21 = ListNode(8)
    # l2 = ListNode(9,l21)
    # # nums.append([4,3,2,7,8,2,3,1])
    # s = Solution()
    # ln= s.mergeTwoLists2(l11,l2)
    # while ln!=None:
    #     print(ln.val)
    #     ln= ln.next
    s = Solution()
    print(s.plusOne([9,9,9,9]))
    # print(s.plusOne([9]))