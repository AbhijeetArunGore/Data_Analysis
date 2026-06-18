class Dog:
    def speak(self):
        return "Dog says: Woof"
class Cat:
    def speak(self):
        return "Cat says: Meow"
class Human:
    def speak(self):
        return "Human says: Hello"
def make_it_speak(living_thing):
    return living_thing.speak()
print(make_it_speak(Dog()))
print(make_it_speak(Cat()))
print(make_it_speak(Human()))

