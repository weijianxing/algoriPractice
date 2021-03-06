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
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        while(head):
            next = head.next
            if head.val == next.val:
                head.next = head.next.next
            head = head.next
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
    def addBinary(self, a: str, b: str) -> str:
        res = ''
        jw = '0'
        len_a = len(a)
        len_b = len(b)
        if len_a > len_b:  # 补全字符串
            b = '0'*(len_a-len_b) + b
        else:
            a = '0'*(len_b-len_a) + a
        for i in range(len(a)-1, -1, -1):
            if (jw == '1')^(a[i] == '1')^(b[i] == '1'):  # 存在一个1或者全为1
                res = '1' + res
                if not (jw == a[i] == b[i] == '1'):
                    jw = '0'
            else:  # 存在一个0或者全为0
                res = '0' + res
                if not (jw == a[i] == b[i] == '0'):
                    jw = '1'
        return res if jw == '0' else '1' + res
    def merge(self, intervals: list) -> list:
        ret = []
        size = len(intervals)
        for i in range(size):
            for j in range (size - i):
                comp = intervals[i]
                if(intervals[i][0]<intervals[j][0] and  intervals[i][1]<intervals[j][1]):
                    comp[0] = intervals[i][0]
                    comp[1] = intervals[j][1]
                    # intervals.remove(intervals[i])
                if(comp[0]<intervals[j][0] and  comp[1]<intervals[j][1]):
                    comp[1] = intervals[j][1]
                    # intervals.remove(intervals[j])
            ret.append(comp)
        return ret
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.climbStairs(n - 1) + self.climbStairs(n - 2) if n > 2 else n
    def sortColors(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]<nums[j]:
                    nums[i] = nums[j]^nums[i]
                    nums[j] = nums[i]^nums[j]
                    nums[i] = nums[j]^nums[i]
        print(nums)
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
    # print(s.plusOne([9,9,9,9]))
    print(s.sortColors([2,0,2,1,1,0]))
    # print(s.plusOne([9]))