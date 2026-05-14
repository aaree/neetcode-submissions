class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1
        deSet=set(deadends)
        seen=set()
        queue=deque()
        queue.append('0000')
        cnt=0
        while queue:
            for i in range(len(queue)):
                curr=queue.popleft()
                if curr==target:
                    return cnt
                arr=list(curr)
                for i, val in enumerate(arr):
                    up=int(val)+1
                    down=int(val)-1
                    if up>9:
                        up-=10
                    if down<0:
                        down+=10
                    old=arr[i]
                    upArr=arr
                    downArr=arr
                    upArr[i]=str(up)
                    upString=''.join(upArr)
                    if upString not in seen and upString not in deSet:
                        queue.append(upString)
                        seen.add(upString)
                    downArr[i]=str(down)
                    downString=''.join(downArr)
                    arr[i]=old
                    if downString not in seen and downString not in deSet:
                        queue.append(downString)
                        seen.add(downString)
            cnt+=1
        return -1
