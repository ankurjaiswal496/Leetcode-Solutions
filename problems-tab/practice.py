from typing import Counter


class Solution:
    def largestIsland(self, grid) :
        # print(len(grid))
        count=0
        flag=0
        for i in range(len(grid)):
            # s=Counter(grid[i])
            # print(grid[i])
            for j in range(len(grid[i])):

                if grid[i][j]==0:
                    flag+=1
                    grid[i][j]+=1
                    break
            if flag==1:
                break
        print(grid)
        for i in range(len(grid)):
            # s=Counter(grid[i])
            
            for j in range(len(grid[i])):
                if grid[i][j]==1:
                    count+=1
        return count
        # print(grid)
            # s=Counter(grid[i])
            # print(s)
        # for i in range(len(grid))
        #     return grid.count(1)

obj=Solution()
print(obj.largestIsland([[1,0,1],[0,0,0],[0,1,1]]))

# a=[1,2]
# print(a.count(2))