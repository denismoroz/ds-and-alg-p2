
### Finding the Square Root of an Integer

Square root search is implemented by using binary search algorithm. 
Square root is for sure is less than a number. Possible outcomes are divided on two parts by middle element.
Middle element is compared if it can be a floored square root of requested number.
If squared middle element is bigger than number then check elements before middle, 
otherwise try to search for answer in elements bigger than middle.
Repeat these steps till square root is found.

### Time and Space complexity

Space complexity: O(1).
Time complexity: O(log n) due to binary search.
 