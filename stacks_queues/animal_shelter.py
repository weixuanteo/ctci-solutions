# An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first out" basis. 
# People must adopt either the "oldest" (based on arrival time) of all animals at the shelter, 
# or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of that type). 
# They cannot select which specific animal they would like. 
# Create the data structures to maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog, and dequeueCat. 
# You may use the built-in LinkedList data structure.
import sys
from singly_linked_list import SinglyLinkedList

class Animal:
    def __init__(self, name):
        self.name = name
        self.order = sys.maxsize

    def __gt__(self, other):
        return self.order > other.order
    
    def __lt__(self, other):
        return self.order < other.order
    
    def __ge__(self, other):
        return self.order >= other.order
    
    def __le__(self, other):
        return self.order <= other.order

    def __eq__(self, other):
        return self.name == other.name
    
    def __str__(self):
        return self.name

class Dog(Animal):
    pass

class Cat(Animal):
    pass

class AnimalQueue:
    def __init__(self):
        self.dogs = SinglyLinkedList()
        self.cats = SinglyLinkedList()
        self.order = 0
    
    def enqueue(self, animal: Animal):
        animal.order = self.order
        self.order += 1
        if isinstance(animal, Dog):
            self.dogs.add_to_tail(animal)
        else:
            self.cats.add_to_tail(animal)
    
    def dequeue_any(self) -> Animal:
        if self.dogs.is_empty() and self.cats.is_empty():
            return None
        elif self.dogs.is_empty():
            return self.cats.remove_from_head().data
        elif self.cats.is_empty():
            return self.dogs.remove_from_head().data
        elif self.dogs.head.data > self.cats.head.data:
            return self.cats.remove_from_head().data
        else:
            return self.dogs.remove_from_head().data
    
    def dequeue_dog(self) -> Dog:
        return self.dogs.remove_from_head().data
    
    def dequeue_cat(self) -> Cat:
        return self.cats.remove_from_head().data