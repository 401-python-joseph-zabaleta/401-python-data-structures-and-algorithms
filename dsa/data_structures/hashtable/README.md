# Hash Table
[Table of Contents](../../../README.md)
## Challenge 30
Implement a HashTable with the following methods:
1. [x] `add`: Takes in both the key and value. This method should hash they key, and add the key and value pair to the table, handling collisions as needed.
2. [x] `get`: Takes in the key and returns the value from the table.
3. [x] `contains`: takes in the key and returns a boolean, indicating if they key exists in the table already.
4. [x] `hash`: takes in an arbitrary key and returns an index in the collection.

## User Tests
1. [x] Adding a key/value to your hashtable results in the value being in the data structure.
2. [x] Retrieving based on a key returns the value stored
3. [x] Successfully return a null for a key that does not exist in the hashtable
4. [x] Successfully handle a collision within the hashtable
5. [x] Successfully retrieve a value from a bucket within the hashtable that has a collision
6. [x] Successfully hash a key to an in-range value

## Approach & Efficiency
Hashmap uses a list, and linkedlists to store data. It has four functions which are Add, Get, Contains, and Hash. When adding items to our hash map this is an O(1) operation unless there is a collision which can result in O(N) for the size of the bucket. When getting a key value, its the same, O(1) lookup time and returning value with O(N) if there was a collision at that key. Contains uses a LinkedList function that traverses the linkedlist at the given map location of our hashmap.

## API
- `add(self, key, value)`:
    - The add function is responsible for adding data to the hashmap.
    - This function consists of O(1) operations inside resulting in an O(1) add time complexity.
- `get(self, key)`:
    - This get function is responsible for returning the value for that key if it exists in the hashmap.
    - It has an initial O(1) lookup time, based on the hashed index value, but if there were any collisions, we encounter an O(N) on a collision.
- `contains(self, key)`:
    - This contains fucntion is responsible for returning a bool for whether or not the provided key is within the data structure.
    - During this function we are using a built in linked list function that creates a collection, which takes up O(N) space. This is mainly if the key we are looking up is stored in a bucket that has had a collision. If no collision, then the lookup time O(1).
- `hash(self, key)`:
    - This is responsible for taking in a key, and passing it through a little hashing algorithm. Its an O(N) for each character in the initial key. This will return an index value used for placing the key into the hashmap itself.

