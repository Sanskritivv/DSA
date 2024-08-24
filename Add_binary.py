class Solution(object):
    def addBinary(self, a, b):
        a = int(a, 2)
        b = int(b, 2)
        res = a+b
        return bin(res)[2:]
