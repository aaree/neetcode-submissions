class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        grouped={}
        for i in strings:
            temp=[]
            for j in i:
                val=ord(j)-ord('a')
                temp.append(val)
            offset=temp[0]
            print(offset)
            print(temp)
            for k in range(len(temp)):
                insert=(temp[k]-offset)
                print(insert)
                if insert<0:
                    insert+=26
                if insert>25:
                    insert-=26
                temp[k]=insert
            temp2=tuple(temp)
            if temp2 not in grouped:
                grouped[temp2]=[]
            grouped[temp2].append(i)
        final=[]
        for key, val in grouped.items():
            final.append(val)
        return final