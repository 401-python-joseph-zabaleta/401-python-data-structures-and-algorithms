# Fizz Buzz Tree
[Table of Contents](../../../README.md)
## Challenge 16
Conduct "FizzBuzz" on a tree while traversing through it. Change the values of each of the nodes dependent on the current node's value.

## Features
- [x] Write a function called `fizz_buzz_tree()` which takes a tree as an argument.
- [x] Determine whether or not the vlaue of each node is divisible by 3, 5, or both. Create a new tree with the same structure as the original but the values modified as follows:
    - [x] If the value is divisible by 3, replace the value with "Fizz".
    - [x] If the value is divisible by 5, replace the vlaue with "Buzz".
    - [x] If the value is divisible by 3 and 5, replace the value with "FizzBuzz"
    - [x] If the value is not divisible by 3 or 5, simply turn the number into a String.
- [x] Return the new tree.

## Approach & Efficiency
This function utlizes a trees built in method, breadth_first(). This method uses a while loop so a big o of O(n) to return a collection of the node values. Then fizz_buzz_tree loops through the collection and creates a new collection of altered values based on fizz buzz rules. O(1) space capacity. After all that, a new tree is created taking up more space. Then we loop through the new collection and add the new values to the new tree and return the new tree. Log(n) and O(1) space.

## Solution
![White Board Image](../../../assets/fizz_buzz_tree.png)
