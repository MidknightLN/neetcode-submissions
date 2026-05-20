class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        l, r = 0, len(tokens)
        # print(ord('0')) # 48
        # print(ord('9')) # 57
        while l < r:
            if tokens[l] in ['+', '-', '*', '/']:
                val_b = stack.pop()
                val_a = stack.pop()
                if tokens[l] == '+':
                    res = str(int(val_a)+int(val_b))
                    stack.append(res)
                elif tokens[l] == '-':
                    res = str(int(val_a)-int(val_b))
                    stack.append(res)
                elif tokens[l] == '*':
                    res = str(int(val_a)*int(val_b))
                    stack.append(res)
                elif tokens[l] == '/':
                    res = str(int(int(val_a)/int(val_b)))
                    stack.append(res)
            else:
                stack.append(tokens[l])
            l += 1
        return int(stack[0])