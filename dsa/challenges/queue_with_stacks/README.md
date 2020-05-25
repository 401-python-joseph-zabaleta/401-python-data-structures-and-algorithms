# Queue with Stacks
[Table of Contents](../../../README.md)
## Challenge 11
Create a brand new `PseudoQueue` class. Do not use an existing Queue. Instead, this PseudoQueue class will implement our standard queue interface (the two methods listed below), but will internally only utilize 2 Stack objects. Ensure that you create your class with the following methods:
- `enqueue(value)` which inserts `value` into the PseudoQueue, using a first-in, first-out approach.
- `dequeue()` which extracts a `value` from the PseudoQueue, using first-in, first-out approach.

The `Stack` instances have only `push`, `pop`, and `peek` methods. You should use your own Stack implementation. Instantiate these Stack objects in your PseudoQueue constructor.

### Example:
----
`enqueue(value)`
|Input|Args|Output|
|:-----|:-----:|-----:|
|`[10]->[15]->[20]`|`5`|`[5]->[10]->[15]->[20]`|
|`empty queue`|`5`|`[5]`

---

`dequeue()`
|Input|Output|Internal State|
|:-----|:-----:|-----:|
|`[5]->[10]->[15]->[20]	`|`20`|`[5]->[10]->[15])`|
|`[5]->[10]->[15]`|`15`|`[5]->[10]`

---
## Approach & Efficiency
When it comes to working with matrixs the first that populates in my brain is nested for loops. Currently this is my only approach to solving such a problem. The outer loop
controls which array or row you are working on. While the inner loop will go through that array or row and count each index.

## Solution
![White Board Image](../../../assets/queue_with_stacks.png)
