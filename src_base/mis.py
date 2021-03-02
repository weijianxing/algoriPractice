__author__ = 'weijx.cpp@gmail.com '

class Solution:
    def maxArea(self, height: list) -> int:
        size = len(height)
        maxa = 0
        for i ,d in enumerate(height):
            for j in range(0,size-i):
                minh = min(d,height[j])
                maxa = max(minh*(j),maxa)
        return maxa
    def maxArea2(self, height):

        a = 0
        for index, X in enumerate(height):
            for j in range(len(height)):
                res = min(X, height[j])
                location = index - j
                a = max(a, res*location)

        return a
    def maxArea3(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        maxArea = 0
        while left < right:
            b = right - left
            if height[left] < height[right]:
                h = height[left]
                left += 1
            else:
                h = height[right]
                right -= 1
            area = b*h
            if maxArea < area:
                maxArea = area
        return maxArea
    def intToRoman(self, num: int) -> str:
        m = [
            ['', 'M', 'MM', 'MMM'],
            ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
            ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
            ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        ]
        d = [1000, 100, 10, 1]
        r = ''
        for k, v in enumerate(d):
            r += m[k][num//v]
            num = num % v
        return r


    def longestCommonPrefix(self, strs: list) -> str:
        minlen = 201
        if strs == None or strs == []:
            return ""
        for sub in strs:
            minlen = min(minlen,len(sub))
        if minlen == 0:
            return ""
        prefix = ''
        size = len(strs)
        if size>200:
            return ""
        for i in range(minlen):
            ch = strs[0][i]
            flag = 0
            for j in range(size) :
                if  ch   == strs[j][i]:
                    flag += 1
                    if flag == size:
                        prefix += ch
                        ch = strs[0][i]
                        # print(ch)
                else:
                    return prefix
        return prefix

    def threeSum(self, nums):
        # 将nums分成三组：zeros，positives，negatives
        zeros, positives, negatives = 0, {}, {}
        for num in nums:
            if num == 0:
                zeros += 1
            elif num > 0:
                positives.setdefault(num, 0)
                positives[num] += 1
            else:
                negatives.setdefault(num, 0)
                negatives[num] += 1

        # 相加为0的三元组可能的组成形式：
        # 3个0，两个负数一个正数，两个正数一个负数，一正一负加一零
        results = []
        if zeros >= 3:
            results.append([0] * 3)

        if len(positives) != 0 and len(negatives) != 0:
            for pi in positives:
                count = positives[pi]
                if count >= 2 and (-2 * pi) in negatives:
                    results.append([pi] * 2 + [-2 * pi])
                if -pi in negatives and zeros > 0:
                    results.append([pi, -pi, 0])
                for pj in positives:
                    if pj <= pi:
                        continue
                    if -1 * (pi + pj) in negatives:
                        results.append([-1 * (pi + pj), pi, pj])

            for ni in negatives:
                count = negatives[ni]
                if count >= 2 and (-2 * ni) in positives:
                    results.append([ni] * 2 + [-2 * ni])
                for nj in negatives:
                    if nj <= ni:
                        continue
                    if -1 * (ni + nj) in positives:
                        results.append([-1 * (ni + nj), ni, nj])

        return results

    def removeDuplicates(self, nums: list) -> int:
        lenth = len(nums)-1
        if lenth > 0:
            for i in range(lenth,0,-1):
                print(i)
                if nums[i] == nums[i-1]:
                    del nums[i]
        return len(nums)


    def searchInsert(self, nums: list, target: int) -> int:
        begininex = 0
        endindex = len(nums)
        while(begininex<endindex):
            mid = begininex + (endindex-begininex)//2
            if nums[mid] > target:
                endindex = mid
            elif nums[mid] < target:
                begininex= mid+1
            else:
                return mid
        return begininex

    def lengthOfLastWord(self, s: str) -> int:
        if s == " ":
            return 0
        ret = 0
        s = s.strip(' ')
        for i in range(len(s)-1, -1,-1):
            if s[i] == ' ':
                return ret
            ret += 1
        return len(s)

if __name__ == '__main__':

    # data = [1,1]
    s = Solution()
    print(s.lengthOfLastWord("a "))

    # strs =[]
    # print(s.longestCommonPrefix(strs))
    # print(s.maxArea3(data))