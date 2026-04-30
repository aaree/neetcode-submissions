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
                #print(curr)
                if curr==endWord:
                    match=True
                    break
                c1={}
                for loc,let in enumerate(curr):
                    c1[(let,loc)]=[loc,c1.get((let,loc),[0,0])[1]+1]
                #print(c1)
                for word in wordList:
                    #print(word)
                    c2={}
                    if word not in seen:
                        c1_test={k: v[:] for k, v in c1.items()}
                        #print(c1_test)
                        #print(c1_test)
                        for loc,let in enumerate(word):
                            c2[(let,loc)]=[loc,c2.get((let,loc),[0,0])[1]+1]
                        print(c2)
                        for key, val in c2.items():                            
                            if key in c1_test:
                                if c1_test[key][0]==c2[key][0]:
                                    #print(key,c1_test[key])
                                    #print(key,c2[key])
                                    c1_test[key][1]=c1_test[key][1]-c2[key][1]
                            #print(c1_test)
                            if c1_test.get(key,(0,0))[1]<=0:
                                if key in c1_test:
                                    del c1_test[key]
                        
                        #print(len(c1_test))
                        if len(c1_test)==1 and word not in seen:
                            for key, val in c1_test.items():
                                if val[1]==1:
                                    #print(word)
                                    #print(c1_test)
                                    seen.add(word)
                                    queue.append(word)
            cnt+=1
            if curr==endWord:
                break

        if match:
            return cnt
        else:
            return 0