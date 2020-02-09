from collections import deque
class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        def create_next_steps(s):
            next_steps = []
            for i in [0,1,2,3]:
                temp = s[0:i] + str((int(s[i]) - 1) % 10) + s[i+1:]
                next_steps.append(temp)
                temp = s[0:i] + str((int(s[i]) + 1) % 10) + s[i+1:]
                next_steps.append(temp)
            return next_steps                                            
        start = "0000"
        if start in deadends:
            return -1
        q = deque()
        visited = dict()
        visited[start] = 0
        q.append(start)
        while len(q) != 0:
            node = q.popleft()
            for item in create_next_steps(node):
                if item == target:
                    return visited[node] + 1
                elif item in visited or item in deadends:
                    pass
                else:
                    q.append(item)
                    visited[item] = visited[node] + 1
        return -1

deadends = ["0201","0101","0102","1212","2002"] 
target = "0202"

#deadends = ["20"] 
#target = "02"
o = Solution()
print o.openLock(deadends, target)
