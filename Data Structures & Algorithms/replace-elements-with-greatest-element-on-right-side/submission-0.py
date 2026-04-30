class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr.reverse()
        val=arr[0]
        arr[0]=-1
        for i in range(1,len(arr)):
            temp=arr[i]
            arr[i]=val
            if val<temp:
                val=temp
        arr.reverse()
        return arr

