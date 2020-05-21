# Linked List Insertions
[Table of Contents](../../../README.md)
## Challenge 08
Extend your LinkedList Class:
- [x] Write a `merge_list(list1, list2)` function that takes in two linked lists as arguments.
    - [x] This function will zip the two lists together alternating between the two lists and return a reference to the head of the zipped list.
### Examples:
`merge_lists(list1, list2)`
|Arg `list1`|Arg `list2`|Output|
|------|-----|------|
|head -> [1] -> [3] -> [2] -> X|head -> [5] -> [9] -> [4] -> X|head -> [1] -> [5] -> [3] -> [9] -> [2] -> [4] -> X|
|head -> [1] -> [3] -> X|head -> [5] -> [9] -> [4] -> X|head -> [1] -> [5] -> [3] -> [9] -> [4] -> X|
|head -> [1] -> [3] -> [2] -> X|head -> [5] -> [9] -> X|head -> [1] -> [5] -> [3] -> [9] -> [2] -> X|


### Unit Tests
1.  [x] Merge two linked lists where list1 and list2 are equal length
2.  [x] Merge two linked lists where list1 is shorter than list2
3.  [x] Merge two linked lists where list1 is longer than list2

## Approach & Efficiency
Big(O) will automatically start off as O(n) because we will have to traverse through the linked lists in order to gather all the values. I was able use the same while loop to iterate over both linked lists at the same time. I used class functions of insert and append to create the new linked list for output. My append class method does use a while loop and this was to maintain the order of each linked list. Since append uses a while loop as well each time, this is also O(n) operation. Big O is now doubled.

## Solution
![White Board Image](../../../assets/ll_merge.png)
