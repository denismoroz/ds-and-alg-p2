
### Search in a Rotated Sorted Array

As input list is sorted, binary search algorithm can be applied on input array with a slight modification. 

While dividing input array on two parts by middle element one of the part 
should be sorted correctly, first element should be less then last one and the other should not.
If part is sorted it is easy to check if search element can be found inside that part,
if yes, then use regular binary search algorithm to find out position, if no skipp it.

Then run recursively algorithm again on part that looks unsorted.
  

### Time and Space complexity

Space complexity: 0(n).
Time complexity: O(log n) due to binary search.
 