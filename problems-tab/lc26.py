class Solution:
    def removeDuplicates(self, nums):
        final=[]
        c=0
        for i in nums:
            if i not in final:
                # print(i)
                final.append(i)
                # print(final)
                c+=1
        final.sort()
        # strings=[str(finals) for finals in final]
        # print(strings)
        # new=",".join(strings)
        # print(new)
        # final_new=
        
        # for j in range(len(nums)-len(final),len(nums)):
        #     final.append('_')
        nums.clear()
        nums=final
        print(nums)
        return c
a=Solution()
print(a.removeDuplicates([1,1,2]))


                
        