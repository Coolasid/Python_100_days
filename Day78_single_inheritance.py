class Animal:
    def __init__(self, name, species) -> None:
        self.name = name
        self.species = species

    def make_sound(self):
        print('Sound made by the animal')

    
class Dog(Animal):
    def __init__(self, name, breed) -> None:
        super().__init__(name, species='Dog')
        self.breed = breed


    # we are overriding the method that comes from Animal
    def make_sound(self):  
        print('Bark!')


d = Dog('Dog', 'xyz')
d.make_sound()

a = Animal('Dog', 'Dog')
a.make_sound()