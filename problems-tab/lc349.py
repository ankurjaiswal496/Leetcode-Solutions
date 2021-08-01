# class Solution(object):
#     def intersection(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: List[int]
#         """
#         res=set()
#         for nums in nums2:
#             if nums in nums1:
#                 res.add(nums)
#         return res
# obj=Solution()
# print(obj.intersection([1,2,2,1],[2,2]))

# def fun(x):
#     return x*5


# a = lambda x: x*5

# print(a(4))



# def fun1(x):
#     assert x!=3, "x should be not be 3"
#     return x


# for i in range(5):
#     try:
#         print(fun1(i))
#     except AssertionError:
#         print("x was 3")


def fun():
    count = 0
    while True:
        count+=1
        yield count


import time
start = time.time()
for i in fun():
    print(i)
    time.sleep(1)
    if i == 5:
        break

print("total time  ",time.time() - start)

