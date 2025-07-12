
Problem link: https://www.geeksforgeeks.org/problems/find-the-longest-string--170645/1

#Brute Force (Using Array) -> TLE 

class Solution():
    def longestString(self, words):
        
        words = sorted(words)
        n = len(words)
        res = ''
        for i in range(n - 1, -1, -1):
            word = words[i]
            for j in range(len(word)):
                prefix = word[: j + 1]
                if prefix not in words:
                    break 
            else:
                if len(word) >= len(res):
                    res = word 
        return res 
                
            
        

#Brute Force (Using Set) -> AC

class Solution():
    def longestString(self, words):
        
        st = set(words)
        
        words = sorted(words)
        n = len(words)
        res = ''
        for i in range(n - 1, -1, -1):
            word = words[i]
            for j in range(len(word)):
                prefix = word[: j + 1]
                if prefix not in st:
                    break 
            else:
                if len(word) >= len(res):
                    res = word 
        return res 
                
            
        

#Optimal (Trie) -> AC 


class TrieNode:
    def __init__(self):
        self.child = {}
        self.isEnd = False 
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.child:
                curr.child[ch] = TrieNode()
            curr = curr.child[ch]
        curr.isEnd = True 
    
        
    def hasAllPrefixes(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.child:
                return False
            curr = curr.child[ch]
            if not curr.isEnd:
                return False
        return True
        
        
class Solution():
    def longestString(self, words):
        
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        res = ''
        for word in sorted(words):
            if trie.hasAllPrefixes(word):
                if len(word) > len(res):
                    res = word
        return res 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

