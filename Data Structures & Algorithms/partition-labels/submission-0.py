class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        c=Counter(s)
        l=r=0
        cnt={}
        ans=[]
        while r<len(s):
            cnt[s[r]]=cnt.get(s[r],0)+1
            check=True
            for a in cnt:
                if cnt[a]!=c[a]:
                    check=False
            r+=1
            if check:
                ans.append(r-l)
                l=r
        return ans