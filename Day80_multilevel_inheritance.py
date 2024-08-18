class Animal:
    def __init__(self, name, species) -> None:
        self.name = name
        self.species = species

    def show_details(self):
        print(f'Name: {self.name}')
        print(f'Species: {self.species}')


class Dog(Animal):
    def __init__(self, name, breed) -> None:
        Animal.__init__(self, name, species='Dog')
        self.breed = breed

    def show_details(self):
        Animal.show_details(self)
        print(f'Breed: {self.breed}')


class GoldenRetriever(Dog):
    def __init__(self, name, color) -> None:
        Dog.__init__(self, name, breed='Golden Retriever')
        self.color = color

    def show_details(self):
        Dog.show_details(self)
        print(f'Color: {self.color}') 



o = GoldenRetriever('tommy', 'black')
o.show_details()
print(GoldenRetriever.mro())