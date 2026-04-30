class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        cnt={}
        for i,val in enumerate(s):
            if val not in cnt:
                cnt[val]=[]
            cnt[val].append(i)
        ans=[]
        print(cnt)
        for key, val in cnt.items():
            interval=[min(val),max(val)]
            ans.append(interval)
        ans.sort()
        final=[]
        for i in ans:
            print(i)
            if len(final)==0:
                final.append(i)
            else:
                if i[0]<=final[-1][1]:
                    final[-1][1]=max(i[1],final[-1][1])
                else:
                    final.append(i)
        final2=[]
        for i in final:
            final2.append(i[1]-i[0]+1)
        return final2