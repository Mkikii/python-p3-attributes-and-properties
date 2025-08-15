#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="Dog", breed="Beagle"):
        self._name = None  
        self._breed = None
        self.name = name      
        self.breed = breed    

    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")
            
    def get_name(self):
        return self._name
    

    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")

    def get_breed(self):
        return self._breed

    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)

    def __str__(self):
        return f"{self._name} | {self._breed}"


Mendoza = Dog("", "French Bulldog")
print(Mendoza)

BadDog = Dog("Spike", "Dragon")
print(BadDog)