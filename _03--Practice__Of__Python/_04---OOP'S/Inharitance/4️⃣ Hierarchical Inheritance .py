class Animal:
    def Speech(self):
        print("Animal Sounds :")

class Cat(Animal):
    def CatSound(self):
        print("Cat Sound : ")

class Dod(Animal):
    def DogSound(self):
        print("Dog Sound : ")

class Cow(Animal):
    def CowSound(self):
        print("Cow Sound : ")

ob = Cow()
ob.Speech()
ob.CowSound()