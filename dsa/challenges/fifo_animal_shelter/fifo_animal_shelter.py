
class Cat:
    """Creates a Cat Animal Object
    """
    def __init__(self, name):
        self.name = name
        self.kind = 'cat'
        self.next = None

class Dog:
    """Creates a Dog Animal Object
    """
    def __init__(self, name):
        self.name = name
        self.kind = 'dog'
        self.next = None

class Bird:
    """Creates a Bird Animal Object. Just for testing
    """
    def __init__(self, name):
        self.name = name
        self.kind = 'bird'
        self.next = None

class AnimalShelter:
    """The AnimalShelter is a queue that only accepts cats and dogs. It keeps track of who comes in first and removes them using the First-in, First-Out principle.
    """
    def __init__(self, front=None):
        self.front = front
        self.rear = self.front


    def __str__(self):
        output = ''
        current = self.front

        while current:
            output += f'[{current.kind}: {current.name}] <- '
            current = current.next
        return output + 'None'

    def enqueue(self, animal):
        """Takes in an animal object argument and adds that value to the back of the queue."""
        if animal.kind in ['cat', 'dog']:
            if self.rear is None:
                self.front = self.rear = animal
            else:
                self.rear.next = animal
                self.rear = self.rear.next
        else:
            raise Exception('We can only accept a cat or a dog.')

    def dequeque(self, pref=None):
        """Takes in a preference of animal to remove and removes them from the front of the queue."""
        if pref is None or pref not in ['cat', 'dog']:
            return None
        else:
            if self.front.kind == pref:
                leaving_animal = self.front
                self.front = self.front.next
                return leaving_animal.name
            else:
                current = self.front
                while current:
                    if current.next.kind == pref:
                        leaving_animal = current.next
                        current.next = current.next.next
                        return leaving_animal.name
                    current = current.next












