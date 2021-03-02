import re

__author__ = 'weijx.cpp@gmail.com '

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    st = {}
    i, ans = 0, 0
    for j in range(len(s)):
        if s[j] in st:
            i = max(st[s[j]], i)
        ans = max(ans, j - i + 1)
        st[s[j]] = j + 1
    return ans

def lengthOfLongestSubstring2( s = "bbbbb"):
    def lcp(s, t):
        n = min(len(s),len(t))
        for i in range(0,n):
            if(s[i] != t[i]):
                return s[0:i]
        else:
            return s[0:n]
    # str = "acbdfghybdf"
    lrs="";
    n = len(s);
    ret = 0
    for i in range(0,n):
        for j in range(i+1,n):
            #Checks for the largest common factors in every substring
            x = lcp(s[i:n],s[j:n])
            #If the current prefix is greater than previous one
            #then it takes the current one as longest repeating sequence
            if(len(x) > len(lrs)):
                lrs=x

    print(len(lrs))
    # print(ret)
    print("Longest repeating sequence: "+lrs)
def longestPalindrome( s: str) -> str:
    #最长子串问题
    #贪心算法
    for j in range(len(s), -1, -1):
        for i in range(len(s)-j, -1, -1):
            if (s[i:i+j]) == s[i:i+j][::-1]:
                return s[i:i+j][::-1]
def reverse(x: int) -> int:
    ret = int(( str(x) if x > 0 else (str(-x) + "-"))[::-1])
    if -2**31<=ret<=2**31-1:
        return ret
    else:
        return 0
def myAtoi(self, s: str) -> int:
    trimstr = str.replace(" ","")
    symbal = '-'
    numbstr =  '0123456789'
    strret = ""
    if len(trimstr)>1 :
        for num in trimstr[1:]:
            if num in num:
                strret += num
            else:
                break
    elif len(trimstr) == 1:
        pass

def myAtoi(self, s: str) -> int:
    # trimstr = re.findall('^[\+\-]?\d+',s.lstrip())
    # if len(trimstr)>0:
    #     int(max(trimstr))
    return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2**31 - 1), -2**31)
def isMatch( s: str, p: str) -> bool:
    return re.fullmatch(p,s)
def strStr( haystack: str, needle: str) -> int:
    return haystack.find(needle)
def isValid( s: str) -> bool:
    if len(s)%2>0:
        return False
    for i in range(0, int(len(s)/2)):
        s = s.replace('()','').replace('[]','').replace('{}','')
    if s == '':
        return True
    else:
        return False

def test():
    for i in range(3,-1,-1):
        print(i)
    print("abc"[::-1])
if __name__ == '__main__':
    print(strStr("hello","lxl"))