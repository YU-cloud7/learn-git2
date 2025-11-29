class Animal:
    def speak(self):
        print("某种动物在叫")
class Dog(Animal):
    def speak(self):
        print("汪汪汪")
class Cat(Animal):
    def speak(self):
        print("喵喵喵")
class Cow(Animal):
    def speak(self):
        print("哞哞哞")
def animal_speak(animal:Animal):
    animal.speak()
dog=Dog()
cat=Cat()
cow=Cow()
generic_animal=Animal()
print("狗的表现：")
animal_speak(dog)
animal_speak(cat)
animal_speak(cow)
animal_speak(generic_animal)
              