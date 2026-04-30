class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans=[]
        seen=set()
        def backtrack(ip,pointer,period,prev_pointer):
            if period==0:
                if ip not in seen:
                    #print(ip[pointer:])
                    if len(ip[pointer:])>0 and int(ip[pointer:])<=255 and not (len(ip[pointer:])>1 and ip[pointer:].startswith('0')):
                        ans.append(ip)
                        seen.add(ip)
                return
            for i in range(pointer,len(ip)):
                if ip[pointer]=='0':
                    newS=ip[:i+1]+'.'+ip[i+1:]
                    backtrack(newS,i+2,period-1,pointer)
                    break
                elif ip[i]!='.' and len(ip[pointer:i+1])>0 and int(ip[pointer:i+1])<=255:
                    newS=ip[:i+1]+'.'+ip[i+1:]
                    print(newS,ip,pointer)
                    backtrack(newS,i+2,period-1,pointer)       
        backtrack(s,0,3,0)
        return ans