class Solution:
    def romanToInt(self, s: str) -> int:
        symbol = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
        value  = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        i = 0
        ans = 0
        while i < len(s):
            if s[i:i+2] in symbol:
                ans += value[symbol.index(s[i:i+2])]
                i += 2
            elif s[i] in symbol:
                ans += value[symbol.index(s[i])]
                i += 1
        return ans