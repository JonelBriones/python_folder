class Pet:
    # implement __init__( name , type , tricks ):
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = 100
        self.health = 100
        # implement the following methods:
        # sleep() - increases the pets energy by 25

    def sleep(self):
        self.energy += 10
        print(f"{self.name}'s energy increased by 25!")
        return self

        # eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
        print(f"{self.name}'s energy increased by 5!")
        self.health += 10
        print(f"{self.name}'s health increased by 10!")
        return self

        # play() - increases the pet's health by 5
    def play(self):
        self.energy += 5
        print(f"{self.name}'s energy increased by 5!")
        return self

        # noise() - prints out the pet's sound
    def noise(self):
        print(f"{self.name}: ZZZzzzzzzz.")
        return self


class Ninja:

    # implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
        # implement the following methods:
        # walk() - walks the ninja's pet invoking the pet play() method

    def walk(self):
        self.pet.play()
        print("Invoking play() Method ")
        print(f"{Jonel.first_name} is walking {ryu.name}")
        return self
        # feed() - feeds the ninja's pet invoking the pet eat() method

    def feed(self):

        self.pet.eat()
        print("Invoking eat() Method ")
        print(f"{Jonel.first_name} is feeding {ryu.name}")
        return self

    def bathe(self):
        print("Invoking noise() Method ")
        print(f"{Jonel.first_name} is bathing {ryu.name}")
        return self


Jonel = Ninja("Jonel", "Briones", "snacks", "kibble", "cane")
ryu = Pet("Ryu", "Mixed", "Sit")
Jonel.feed()
