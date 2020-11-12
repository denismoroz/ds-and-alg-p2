#!/usr/bin/env python
# coding: utf-8

# # Building a Trie in Python
# 
# Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.
# 
# Before we move into the autocomplete function we need to create a working trie for storing strings.  We will create two classes:
# * A `Trie` class that contains the root node (empty string)
# * A `TrieNode` class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.
# 
# Give it a try by implementing the `TrieNode` and `Trie` classes below!

# In[1]:


import collections


# Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False
    
    def insert(self, char):
        return self.children[char]


# The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current_node = self.root
        
        for char in word:
            current_node = current_node.insert(char)
            
        current_node.is_word = True

    def find(self, prefix):
        # Find the Trie node that represents this prefix
        if not isinstance(prefix, str):
            raise ValueError("Please, provide string as input parameter")

        current_node = self.root

        for char in prefix:
            if char not in current_node.children:
                return None
            current_node = current_node.children[char]

        return current_node


# # Finding Suffixes
# 
# Now that we have a functioning Trie, we need to add the ability to list suffixes to implement our autocomplete
# feature.  To do that, we need to implement a new function on the `TrieNode` object that will return all complete word
# suffixes that exist below it in the trie.  For example, if our Trie contains the words
# `["fun", "function", "factory"]` and we ask for suffixes from the `f` node, we would expect to receive
# `["un", "unction", "actory"]` back from `node.suffixes()`.
# 
# Using the code you wrote for the `TrieNode` above, try to add the suffixes function below.
# (Hint: recurse down the trie, collecting suffixes as you go.)

# In[5]:

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False
    
    def insert(self, char):
        return self.children[char]
        
    def suffixes(self, suffix=''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        result = []
        
        if self.is_word and suffix:
            result.append(suffix)

        for char, node in self.children.items():
            result += node.suffixes(suffix+char)
            
        return result


# # Testing it all out
# 
# Run the following code to add some words to your trie and then use the interactive search box to see what your code returns.

# In[6]:


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


def testFunction(prefix, expectation):
    prefixNode = MyTrie.find(prefix)

    result = prefixNode.suffixes() if prefixNode else []

    if expectation == result:
        print('Pass')
    else:
        print('Fail')


testFunction('a', ['nt', "nthology", "ntagonist", "ntonym"]) # Pass
testFunction('fun', ["ction"]) # Pass
testFunction('trip', ["od"])# Pass

#Edge cases

testFunction('', wordList) # Pass
testFunction('z', []) # Pass

try:
    testFunction(None, [])
except ValueError as e:
    print(e)



