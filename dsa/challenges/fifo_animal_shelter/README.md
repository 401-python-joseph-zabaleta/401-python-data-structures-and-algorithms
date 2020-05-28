# First-in, First out Animal Shelter.
[Table of Contents](../../../README.md)
## Challenge 12
Create a class called AnimalShelter which holds only dogs and cats. The shelter operates using a first-in, first-out approach.
Implement the following methods:
- `enqueue(animal)`: adds `animal` to teh shelter. `animal` can be either a dog or a cat object.
- `dequeue(pref)`: returns either a dog or a cat. If `pref` is not `dog` or `cat` then return `None`.
---
## Approach & Efficiency
This is not the best solution for managing a queue. Utilizing two stacks to "slinking" between in order to maintain the First-In-First-Out is a Big-O Nightmare. I had to utilize a while loop, to iterate over the first stack to retreive the bottom, or first out node. Then reverse the process to return the stack back to normal so any additional items added to the queue were after those already placed in queue.

---

## Solution
![White Board Image](../../../assets/fifo_animal_shelter.png)
