class Animal:
    def  speak(self):
        print("某种动物在叫")
class Dog(Animal):
    def speak(self):
        print("汪汪汪")
class Cat(Animal):
    def speak(self):
        print("喵喵喵")
dog=Dog()
cat=Cat()
dog.speak()
cat.speak()