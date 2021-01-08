class Solution(object):
    def findCircleNumRc(self,i,isConnected,isVisited):
        """
        广度优先搜索
        :param i:
        :return:
        """
        l = []
        l.append(i)
        while len(l) > 0:
            index = l.pop()
            isVisited[index] = True
            connected = [item for item in range(len(isConnected)) if isConnected[index][item] == 1 and item != i]
            for item in connected:
                if item not in l and not isVisited[item]:
                    l.append(item)
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        isVisited = [False for i in range(n)]
        num = 0
        for i in range(n):
            if not isVisited[i]:
                num += 1
                self.findCircleNumRc(i,isConnected,isVisited)
        return num

s = Solution()
v = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
num = s.findCircleNum(v)
print(num)

# 1 0 0 1
# 0 1 1 0
# 0 1 1 1
# 1 0 1 1