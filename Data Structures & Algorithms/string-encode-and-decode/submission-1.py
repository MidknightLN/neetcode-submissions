class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s))+'#'+ s
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        temp = ''
        count = 0
        L = len(s)
        while count < L:
            if s[count].isdigit():
                temp += s[count]
                count += 1
            elif s[count] == '#' and temp.isdigit():
                res.append(s[count+1:count+1+int(temp)])
                count += int(temp) +1
                temp = ''
            
        return res