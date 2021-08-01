class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if not nums2:
            return nums1
        else:
            for i in range(0,m):
                
                    nums1.append(nums2[i])
        nums1.sort()
        while 0 in nums1:
            nums1.remove(0)
        return nums1
obj=Solution()
print(obj.merge([0],0,[1],1)) 
