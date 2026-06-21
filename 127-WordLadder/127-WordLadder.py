# Last Updated: 6/22/2026, 12:43:41 AM
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordlist=set(wordList)
        if endWord not in  wordList:
            return 0
        q=deque([(beginWord,1)])
        alphas=['a','b','c','d','e','f','g','h','i','j','k','l','m',
                'n','o','p','q','r','s','t','u','v','w','x','y','z']
        while q:
            word,count=q.popleft()
            if word==endWord:
                return count
            for i in range(len(word)):
                for let in alphas:
                    new_word=word[:i]+let+word[i+1:]
                    if new_word in wordlist:
                        q.append((new_word,count+1))
                        wordlist.remove(new_word)
        return 0
