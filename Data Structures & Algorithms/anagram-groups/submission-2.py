class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=[]
        seen=set()
        def is_anagram(s,t):
            if len(s)!=len(t):
                return False
            if len(s)==len(t)==0:
                return True
            dicS={}
            dicT={}
            for i in range(len(s)):
                dicS[s[i]]=dicS.get(s[i],0)+1
                dicT[t[i]]=dicT.get(t[i],0)+1
            return dicS==dicT
        for i in range(len(strs)):
            if strs[i] in seen:
                continue
            ana=[strs[i]]
            for j in range(len(strs)):
                if is_anagram(strs[i],strs[j])==True and i!=j:
                    ana.append(strs[j])
                    seen.add(strs[j])
            ans.append(ana)
        return ans