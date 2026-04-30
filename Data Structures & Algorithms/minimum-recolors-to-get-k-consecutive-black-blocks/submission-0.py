class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        cnt=0
        l=r=0
        min_cnt=999999999
        while r<len(blocks):
            if blocks[r]=='W':
                cnt+=1
            while r-l+1>k:
                if blocks[l]=='W':
                    cnt-=1
                l+=1
            if r-l+1==k:
                min_cnt=min(cnt,min_cnt)
            r+=1
        return min_cnt