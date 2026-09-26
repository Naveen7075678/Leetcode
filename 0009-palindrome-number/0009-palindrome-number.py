class Solution:
    def isPalindrome(self, n: int) -> bool:
        number = 0
        original = n
        while n>0:
            a = n%10
            number = number*10 +a
            n = n//10

        if number == original :
            return True
        else:
            return False
a = Solution()
obj = a.isPalindrome(202)
print(obj)