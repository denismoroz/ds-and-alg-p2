
### Autocomplete with Tries

Autocomplete is implemented with using tree of TrieNodes. Each node contains a character 
and hash of it's children and a flag if this node is represent the end of the word.

### Time and Space complexity

Space complexity: 
    Insert: O(n) where n number of nodes in a tree.
    Search: O(n) where n is word length
    
Time complexity: 
    Insert: O(n) where n is word length.
    Search: O(n) where n is search word length
     