class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        reverse = 0
        while x > 0:
              
            a = x % 10
            if reverse > 214748364:
                return 0

            if reverse == 214748364 and a > 7:
               return 0
            reverse = reverse *10 + a
            x = x//10

        return reverse*sign

