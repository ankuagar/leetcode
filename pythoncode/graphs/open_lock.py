from collections import deque
import time
class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        start = "0000"
        if start in deadends:
            return -1
        q = deque()
        visited = set()
        q.append(start)
        visited.add(start)
        step = 0       
        while len(q) != 0:
            step += 1
            qsize = len(q)
            for i in xrange(qsize):
                s = q.popleft()
                for i in xrange(len(start)):
                    temp1 = s[0:i] + str((int(s[i]) - 1) % 10) + s[i+1:]
                    temp2 = s[0:i] + str((int(s[i]) + 1) % 10) + s[i+1:]
                    for item in [temp1, temp2]:
                        if item == target:
                            return step
                        elif item in visited or item in deadends:
                            pass
                        else:
                            q.append(item)
                            visited.add(item)
        return -1

deadends = ["0201","0101","0102","1212","2002"] 
target = "0202"

#deadends = ["20"] 
#target = "02"
o = Solution()
print o.openLock(deadends, target)
