class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l=0
        r=len(people)-1
        people.sort()
        count=0
        while r>=l:
            total=people[l]+people[r]
            if r==l:
                count+=1
                r-=1
                l+=1
            elif total<=limit:
                count+=1
                l+=1
                r-=1
            elif total>limit:
                count+=1
                r-=1
        return count