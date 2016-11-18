from chapter_03.src.answer_06 import AnimalShelter
import unittest
#In [1]: a = AnimalShelter()
#In [1]: a.enqueue("cat","Bran")
#In [1]: a.dequeue_dog()

class TestAnimalShelter(unittest.TestCase):
    def test_enqueue(self):
        shelter = AnimalShelter()
        shelter.enqueue("cat", "Bran")
        pet = shelter.dequeue_any()
        self.assertEqual(pet._name, "Bran")
        shelter.enqueue("cat", "Jon")
        pet = shelter.dequeue_any()
        self.assertEqual(pet._name, "Jon")

    def test_dequeue_any(self):
        shelter = AnimalShelter()
        shelter.enqueue("cat", "Bran")
        shelter.enqueue("cat", "Jon")
        pet = shelter.dequeue_any()
        self.assertEqual(pet._name, "Bran")
        shelter.enqueue("dog", "Luke")
        pet = shelter.dequeue_any()
        self.assertEqual(pet._name, "Jon")
        shelter.enqueue("cat", "Jazz")
        pet = shelter.dequeue_any()
        self.assertEqual(pet._name, "Luke")

    def test_dequeue_pet(self):
        shelter = AnimalShelter()
        shelter.enqueue("cat", "Bran")
        shelter.enqueue("cat", "Jon")
        shelter.enqueue("cat", "Jazz")
        shelter.enqueue("dog", "Luke")
        shelter.enqueue("dog", "Don")
        pet = shelter.dequeue_dog()
        self.assertEqual(pet._name, "Luke")
        pet = shelter.dequeue_cat()
        self.assertEqual(pet._name, "Bran")
        pet = shelter.dequeue_cat()
        self.assertEqual(pet._name, "Jon")

    def test_dequeue_pet(self):
        shelter = AnimalShelter()
        shelter.enqueue("cat", "Bran")
        shelter.enqueue("cat", "Jon")
        shelter.enqueue("cat", "Jazz")
        shelter.enqueue("dog", "Luke")
        shelter.enqueue("dog", "Don")
        pet = shelter.dequeue_any()
        self.assertEqual(pet._name, "Bran")
        pet = shelter.dequeue_dog()
        self.assertEqual(pet._name, "Luke")
        pet = shelter.dequeue_cat()
        self.assertEqual(pet._name, "Jon")
        pet = shelter.dequeue_any()
        self.assertEqual(pet._name, "Jazz")

if __name__=="__main__":
    unittest.main()