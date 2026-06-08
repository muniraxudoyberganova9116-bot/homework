# Model a Farm

# In this assignment, you’ll create a simplified model of a farm. As you work through this assignment, 
# keep in mind that there are a number of correct answers.

# The focus of this assignment is less about the Python class syntax and more about software design in general, which is highly subjective. 
# This assignment is intentionally left open-ended to encourage you to think about how you would organize your code into classes.

# Before you write any code, grab a pen and paper and sketch out a model of your farm, identifying classes, attributes, and methods. 
# Think about inheritance. How can you prevent code duplication? Take the time to work through as many iterations as you feel are necessary.

# The actual requirements are open to interpretation, but try to adhere to these guidelines:

#     You should have at least four classes: the parent Animal class, and then at least three child animal classes that inherit from Animal.
#     Each class should have a few attributes and at least one method that models some behavior appropriate for a specific animal or all animals
#     —such as walking, running, eating, sleeping, and so on.
#     Keep it simple. Utilize inheritance. Make sure you output details about the animals and their behaviors.

class Animal:
    def __init__(self, name, age, sound, energy):
        self.__name = name
        self.__age = age
        self.__sound = sound
        self.__energy = energy
    
    @property
    def name(self):
        return self.__name  
    @property
    def age(self):
        return self.__age
    @property
    def sound(self):
        return self.__sound
    @property       
    def energy(self):
        return self.__energy    
    
    def eat(self, food):
        self.__energy += food
        print(f"{self.__name} is eating and gaining {food} energy. Total energy: {self.__energy}")

    def sleep(self, hours):
        self.__energy += hours * 2
        print(f"{self.__name} is sleeping for {hours} hours and gaining {hours * 2} energy. Total energy: {self.__energy}")
    
    def speak(self):
        print(f"{self.__name} says: {self.__sound}")    

class Cow(Animal):
    def __init__(self, name, age, energy, milk_gallons=0):
        super().__init__(name, age, "Moo", energy)
        self.__milk_gallons = milk_gallons

    @property
    def milk_gallons(self):
        return self.__milk_gallons
    def produce_milk(self, gallons):
        self.__milk_gallons += gallons
        print(f"{self.name} produced {gallons} gallons of milk. Total milk: {self.__milk_gallons} gallons")

class Chicken(Animal):
    def __init__(self, name, age, energy, egg_count=0):
        super().__init__(name, age, "Cluck", energy)
        self.__egg_count = egg_count

    @property
    def egg_count(self):
        return self.__egg_count

    def lay_egg(self, count):
        self.__egg_count += count
        print(f"{self.name} laid {count} eggs. Total eggs: {self.__egg_count}")

class Dog(Animal):
    def __init__(self, name, age, energy, breed):
        super().__init__(name, age, "Woof", energy)
        self.__breed = breed

    @property
    def breed(self):
        return self.__breed
    
    def herd(self):
        print(f"{self.name} is herding  the other animals. And lost {self.energy * 0.1} energy.")

class Farm:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} the {type(animal).__name__} has been added to the farm.")

    def show_animals(self):
        print("Animals on the farm:")
        for animal in self.animals:
            print(f"{animal.name} the {type(animal).__name__}, Age: {animal.age}, Energy: {animal.energy}")
    
    def feed_animals(self, food):
        print(f"Feeding all animals with {food} food.")
        for animal in self.animals:
            animal.eat(food)

    def daily_routine(self):
        for animal in self.animals:
            animal.eat(10)
            animal.sleep(2)
            animal.speak()
            if isinstance(animal, Cow):
                animal.produce_milk(5)
            elif isinstance(animal, Chicken):
                animal.lay_egg(3)
            elif isinstance(animal, Dog):
                animal.herd()

# Example usage:
if __name__ == "__main__":
    farm = Farm()
    cow = Cow("Bessie", 5, 50)
    chicken = Chicken("Clucky", 2, 30)
    dog = Dog("Rover", 3, 40, "Border Collie")

    farm.add_animal(cow)
    farm.add_animal(chicken)
    farm.add_animal(dog)

    farm.daily_routine()
    farm.feed_animals(20)
    farm.show_animals()