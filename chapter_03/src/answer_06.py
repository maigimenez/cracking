from collections import deque

class Animal:
    def __init__(self, type="cat", name="Tabs"):
        self._type = type
        self._name = name

    def __str__(self):
        return "{} ({})".format(self._name, self._type)


class AnimalShelter:
    def __init__(self):
        self._dogs = deque()
        self._cats = deque()
        self._oldest = deque()

    def enqueue(self, type, name):
        if type == 'cat':
            self._cats.append(Animal(type, name))
        else:
            self._dogs.append(Animal(type, name))

        self._oldest.append(type)

    def dequeue_any(self):
        if self._oldest:
            pet_type = self._oldest.popleft()
            if pet_type == 'cat':
                return self._cats.popleft()
            else:
                return self._dogs.popleft()

    def dequeue_dog(self):
        self._oldest.remove('dog')
        return self._dogs.popleft()

    def dequeue_cat(self):
        self._oldest.remove('cat')
        return self._cats.popleft()

    def __str__(self):
        str_to_print = ""
        cat_index, dog_index = 0, 0
        for pet_type in self._oldest:
            if pet_type == 'cat':
               str_to_print += "{} (cat)\n".format(self._cats[cat_index]._name)
               cat_index += 1
            else:
                str_to_print += "{} (dog)\n".format(self._dogs[dog_index]._name)
                dog_index += 1

        return str_to_print