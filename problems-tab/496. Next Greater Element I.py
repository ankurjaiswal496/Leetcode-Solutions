class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        count=0
        res=[]
        for i in nums1:
            a=nums2.index(i)
            b=a
            # print('hey')
            # print(a)
            # print(len(nums2))
            if a+1==len(nums2):
                res.append(-1)
                print("h")
            print(len(nums2)-a)
            for i in range(1,len(nums2)-a):    
          
                    
                 if nums2[a]<nums2[b+i]:
                            count=nums2[b+i]
                            # print(count)
                            # print('a')
                            pass
                    # print(res)
                 else:
                        res.append(-1)
                    # print(res)
            res.append(count)
                    
         

        return res



obj=Solution()
print(obj.nextGreaterElement([1,3,5,2,4],[6,5,4,3,2,1,7]))


