from collections import deque
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
        q.append((start,0))
        visited.add(start)      
        while len(q) != 0:
            s, length = q.popleft()
            for i in xrange(len(s)):
                temp1 = s[0:i] + str((int(s[i]) - 1) % 10) + s[i+1:]
                temp2 = s[0:i] + str((int(s[i]) + 1) % 10) + s[i+1:]
                for item in [temp1, temp2]:
                    if item == target:
                        return length + 1
                    elif item in visited or item in deadends:
                        pass
                    else:
                        q.append((item, length +1))
                        visited.add(item)
        return -1

deadends = ["0201","0101","0102","1212","2002"] 
target = "0202"

#deadends = ["20"] 
#target = "02"
o = Solution()
print o.openLock(deadends, target)
