#-*- coding: utf-8 -*-
# 
# __author__ : jianxing.wei

def binarySearch(data: list, target):

    size = len(data)
    mid = data[size//2]
    print( mid )
    if target>mid:
        return binarySearch(data[size//2+1:],target)
    elif target == mid:
        return target
    else:
        return binarySearch(data[:size // 2 - 1], target)
    #not find target.
    return -1


def binarySearchw(data: list, target):

    size = len(data)

    begin = 0;
    end = size-1;


    #not find target.
    while begin !=(size-1) or end != 0:
        mid = (begin + end +1) // 2
        if target > data[mid]:
            begin = mid + 1
            end = size;
        elif target == data[mid]:
            return mid
        else:
            end = mid -1

def swap(a,b):
    a = a^b
    b = a^b
    a = a^b
    print(a)
    print(b)

def swap2(a,b):
    a = a&b
    b = a&b
    a = a&b
    print(a)
    print(b)

if __name__ == "__main__":
    data = [2,4,7,8,12, 14,16,20,21]
    # print(1//2)
    # print(data[4:])
    # print("result:")
    # print(binarySearchw(data, 8))
    swap2(2,3)