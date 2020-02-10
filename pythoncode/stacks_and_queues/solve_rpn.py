class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        data = []
        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                data.append(int(token))
            else:
                op2 = data.pop()
                op1 = data.pop()
                if token == '/':
                    if op1 < 0 and op2 > 0:
                        value = (abs(op1) / abs(op2)) * -1
                    elif op2 < 0 and op1 > 0:
                        value = (abs(op1) / abs(op2)) * -1
                    else:
                        value = op1 / op2
                elif token == '*':
                    value = op1 * op2
                    
                elif token == '+':
                    value = op1 + op2
                else:
                    value = op1 - op2
                data.append(value)
        return int(data[0])
obj = Solution()        
#print obj.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
#print obj.evalRPN(["-3", "9","*"])
print obj.evalRPN(["2","1","+","3","*"])


