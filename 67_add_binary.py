class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        a = int(a, 2)
        b = int(b, 2)

        while b:
            without_carry = a^b
            carry = (a & b) << 1
            a,b = without_carry , carry
        
        return bin(a)[2:]

#Time complexity: O(A+B)
#Space complexity: O(1)
