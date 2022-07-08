import unittest

from animal_shelter import Dog, Cat, AnimalQueue


class TestAnimalShelter(unittest.TestCase):
    def test_animal_shelter(self):
        shelter = AnimalQueue()
        shelter.enqueue(Dog("Fido"))
        shelter.enqueue(Cat("Garfield"))
        shelter.enqueue(Dog("Spot"))
        self.assertEqual(shelter.dequeue_any(), Dog("Fido"))
        self.assertEqual(shelter.dequeue_dog(), Dog("Spot"))
        self.assertEqual(shelter.dequeue_cat(), Cat("Garfield"))
        self.assertEqual(shelter.dequeue_any(), None)
