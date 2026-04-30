class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        cnt=0
        seen=set()
        for i in emails:
            email=i.split('@')
            email2=email[0].split('+')
            email3=''.join(email2[0].split('.'))
            final=email3+'@'+email[1]
            if final not in seen:
                seen.add(final)
                cnt+=1
        return cnt