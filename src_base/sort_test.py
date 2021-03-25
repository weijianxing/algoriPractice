#-*- coding: utf-8 -*-
# 
# __author__ : jianxing.wei

class Sort():
    def __init__(self):
        pass
    def quick_sort(self, data) ->list:
        #核心D&C 分解出 基线条件 和 推理通用条件
        if len(data)<2:
            return data
        else:
            pivot = data[0]
            less = [i for i in data[1:] if i<=pivot]
            greater = [i for i in data[1:] if i> pivot]
            return self.quick_sort(less) + [pivot] + self.quick_sort(greater)

if __name__ == '__main__':
    s = Sort()
    data = [7,8,1,4 ,22,9]
    print(s.quick_sort(data))