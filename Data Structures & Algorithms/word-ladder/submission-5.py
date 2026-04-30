class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        exists=False
        seen=set()
        for word in wordList:
            if word==endWord:
                exists=True
        if not exists:
            return 0
        queue=deque()
        queue.append(beginWord)
        seen.add(beginWord)
        cnt=0
        match=False
        while len(queue)>0:
            for i in range(len(queue)):
                curr=queue.popleft()
                if curr==endWord:
                    match=True
                    break
                for word in wordList:
                    if word not in seen:
                        diff = sum(1 for a, b in zip(curr, word) if a != b)
                        if diff == 1:
                            seen.add(word)
                            queue.append(word)                         

            cnt+=1
            if curr==endWord:
                break

        if match:
            return cnt
        else:
            return 0