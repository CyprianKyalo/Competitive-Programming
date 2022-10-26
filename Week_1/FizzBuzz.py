class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        l = []
        
        def div_3(num):
            res = 0
            n = str(num)
            if num < 10 and (num % 3 == 0):
                return True
            else:
                for i in range(len(str(num))):
                    res += int(n[i])
                if res % 3 == 0:
                    return True
            return False
        
        def div_5(num):
            num = str(num)
            if num[-1] == '0' or num[-1] == '5':
                return True
            return False
        
        for i in range(1, n+1):
            if div_3(i) and div_5(i):
                l.append("FizzBuzz")
                # continue
            elif div_3(i):
                l.append("Fizz")
            elif div_5(i):
                l.append("Buzz")
            else:
                l.append(str(i))
        
        return l
                
        