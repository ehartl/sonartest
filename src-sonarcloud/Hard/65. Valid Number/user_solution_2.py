class Solution:
    r
    def is_uinteger(self, st):
        if st=="": return False
        return set(st).issubset("0123456789")
    def is_integer(self,st):
        if st=="": return False
        if st[0] in "+-":
            return self.is_uinteger(st[1:])
        return self.is_uinteger(st)
    def is_decimal(self,st):
        if st=="": return False
        for c,ss in enumerate(st):
            if ss==".": break 
        else: 
            return self.is_integer(st) 
        left = st[:c]
        right = st[c+1:]
        return (((left in "+-") and self.is_uinteger(right)) or
               ((self.is_integer(left) and (self.is_uinteger(right) or right==""))))
    def isNumber(self, s: str) -> bool:
        for c,ss in enumerate(s):
            if ss in "eE":
                break 
        else:
            return self.is_decimal(s) or self.is_integer(s)
        return  self.is_decimal(s[:c]) & self.is_integer(s[c+1:])
