
Problem link: https://leetcode.com/problems/implement-trie-prefix-tree/description/

#Brute Force (Using Array)

class Trie:

    def __init__(self):
        self.arr = []
        

    def insert(self, word: str) -> None:
        self.arr.append(word)
        

    def search(self, word: str) -> bool:
        if word in self.arr:
            return True 
        return False 
        

    def startsWith(self, prefix: str) -> bool:
        for word in self.arr:
            for i in range(len(word)):
                if word[: i + 1] == prefix:
                    return True 
        return False 
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)



#Optimal (Using Trie Data Structure)
class TrieNode:
    def __init__(self):
        self.child = {}
        self.isEnd = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        curr = self.root 
        for ch in word:
            if ch not in curr.child:
                curr.child[ch] = TrieNode()
            curr = curr.child[ch]
        curr.isEnd = True 
        

    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            if ch not in curr.child:
                return False 
            curr = curr.child[ch]
        return True if curr.isEnd else False 

        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            if ch not in curr.child:
                return False 
            curr = curr.child[ch]
        return True 
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
