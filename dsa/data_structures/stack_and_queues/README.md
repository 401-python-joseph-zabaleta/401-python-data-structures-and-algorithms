# Stacks and Queues
[Table of Contents](../../../README.md)
## Challenge 10
This challenge deals with the Call stack and queue. We will be creating a Stack Class and a Queue Class with several methods to manipulate / simulate the stack and queue.

### Unit Tests
#### Stack Tests
- [x] Can successfully push onto a stack.
- [x] Can successfully push multiple values onto a stack.
- [x] Can successfully pop off the stack.
- [x] Can successfully empty a stack after multiple pops.
- [x] Can successfully peek the next item on the stack.
- [x] Can successfully instantiate an empty stack.
- [x] Calling pop or peek on empty stack raises an exception.
#### Queue Tests
- [x] Can successfully enqueue into a queue.
- [x] Can successfully enqueue multiple values into a queue.
- [x] Can successfully dequeue out of a queue the expected value.
- [x] Can successfully peek into a queue, seeing the expected value.
- [x] Can successfully empty a queue after multiple dequeues.
- [x] Can successfully instantiate an empty queue.
- [x] Calling dequeue or peek on empty queue raises exception.

## Approach & Efficiency
Both Stack and Queue Class utilize similiar functions. All functions are running a bigO of O(1). This is because we are doing single functions. We are not having to loop through a list which would result in a bigO of O(n). Space is also O(1). We are able to maintain the space of O(1) due to the fact we not duplicating or making a copy of the list.

## API
### Class Stack:
- `push(self, item)`
    - Takes in any value as an argument and adds a new node with that value to the top of the stack with an O(1) Time performance.
- `pop(self)`
    - Takes no arguments, removes the node from the top of the stack, and returns the node's value.
    - Will raise an exception when called on an empty stack.
- `peek(self)`
    - Takes no arguments and returns the value of the node located on top of the stack, without removing it from the stack.
- `is_empty(self)`
    - Takes no arguments, and returns a boolean indicating whether or not the stack is empty.

### Class Queue:
- `enqueue(self, item)`
    - Takes any value as an argument and adds a new node with that value to the back of the queue with an O(1) Time Performance.
- `dequeue(self)`
    - Takes no arguments, remove the node from the front of the queue, and returns the node's value.
- `peek(self)`
    - Takes no arguments and returns the value of the node located in the front of the queue, without removing it from the queue.
- `is_empty(self)`
    - Takes no arguments and returns a boolean indicating whether or not the queue is empty.
