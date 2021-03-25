__author__ = 'weijx.cpp@gmail.com '

class Solution():
    # def __init__(self,src,n):
    #     self.src=src
    #     self.n=n

    def findDisappearedNumbers2(self, nums: list)->list:
        def swap(nums, i,j):
            nums[i]= nums[i] ^ nums[j]
            nums[j]= nums[i] ^ nums[j]
            nums[i]= nums[i] ^ nums[j]
        for i in range(len(nums)):
            while nums[i] != nums[nums[i]-1]:
                swap(nums, nums[i]-1,i)
        result= []
        print(nums)

        for i in range(len(nums)):
            if nums[i] != i+1:
                result.append(i+1)
        return result
    def findDisappearedNumbers(self, nums: list)->list:
        n = len (nums)
        for num in nums:
            x = (num - 1)%n
            nums[x] += n
        ret = []
        for key, value in enumerate(nums):
            if value<=n:
                ret.append(key + 1)
        return ret

    def twoSum(self,nums: list ,target:int)->list:
        result = {}
        for i, num in enumerate(nums):
            if target - num in result:
                return [result[target-num],i]
            result[num] = i
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        nums = nums1 + nums2
        size = len(nums)
        arr = []
        for n1 in nums1:
            for n2 in nums2:
                pass
    def maxProfit(self, prices: list) -> int:
        size = len(prices)
        buyprice = prices[0]
        maxprof = 0
        for i in range(1, size):
            buyprice = min(prices[i],buyprice)
            maxprof = max(maxprof, prices[i] - buyprice)
        return maxprof







if __name__ == '__main__':
    nums =  [7,1,5,3,6,4]
    # nums.append([4,3,2,7,8,2,3,1])
    s = Solution()
    print(s.maxProfit(nums))




