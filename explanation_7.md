
### HTTPRouter using a Trie

Router core is Trie build based on path parts, that helps to reduce memory usage
and increase lookup time.


### Time and Space complexity

Space complexity: 
    Insert: O(n) where n number of nodes in a trie.
    Search: O(n) where n number of segments in path
    
Time complexity: 
    Insert: O(n) where n number of segments in path.
    Search: O(n) where n number of segments in path, each segment should be checked.
     