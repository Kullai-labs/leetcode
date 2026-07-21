class Solution:
    def reverseBits(self, n: int) -> int:
        b=f"{n:032b}"
        r=b[::-1]
        return int(r,2)
        