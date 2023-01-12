# print(type(1))
# print(type(""))



# Klasser brukar ite använda snake_kase 
# utan de använder Capword/PascalCase
class Animal:
    sound: str = "Growwwr"

    def __init__(self, sound: str):
        self.sound = sound
        pass

    def speak(self):
        print("I say " + self.sound)
        return "I say " + self.sound

    def change_sound(self, sound = str): 
        self.sound = sound
    
    def get_sound(self):
        return self.sound
    

class Coumputerscreen:
    pass

animal = Animal("")
cat = Animal("Mjau")
dog = Animal("Voff")
fish = Animal("Blubb")
screen = Coumputerscreen()
#car = Vehicle()


animal.change_sound("Prassel")
animal.sound = "Growwwr"
# print(animal.sound)
# print(cat.sound)
# print(dog.sound)
# print(fish.speak())

class Company:
    name: str
    number_of_employees: int
    adress: str
    CEO: str
    def __init__(self, name: str, number_of_employees: int, adress: str, ceo: str):
        self.name = name
        self.number_of_employees = number_of_employees
        self.adress = adress
        self.CEO = ceo
    
    def __str__(self) -> str:
        name_string = f"Name: {self.name}"
        adress_string = f"Adress: {self.adress}"
        employees_string = f"Employees: {self.number_of_employees}"
        ceo_string = f"CEO: {self.CEO}"
        return f"{name_string}, {adress_string}, {employees_string}, {ceo_string}"

class Person:
    first_name: str
    last_name: str
    age: int
    height: int
    full_name: str
    company: Company

    def __init__(self, first_name: str, last_name: str, age: int, height: int, company: Company):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.company = company
        self.full_name= f"{first_name} {last_name}"

    def __str__(self) -> str:
        return f"Hej, jag heter {self.first_name} {self.last_name}, är {self.age} år gammal och {self.height} cm lång."

    def __int__(self):
        return self.first_name.count("A")


adam = Person("Adam", "Sultan", 25, 184, Company(
    "Avarn", 4, "Någonstans in Stockholm", "Adam Sultan"))

# print(adam.first_name)
# test = int(adam)
# print(test)
# print(adam)
# print(adam.company)


class Phone:
    number: str
    weight: int
    manufacturer: str
    color: str
    five_G_enabled: bool

    def __init__(self, number: str, weight: int, manufacturer: str, color: str, five_G_enabled: bool):
        self.color = color
        self.number = number
        self.weight = weight
        self.manufacturer = manufacturer
        self.five_G_enabled = five_G_enabled
        
class SmartPhone(Phone): 
    apps: list[str]
    foldable: bool

    def __init__(self, apps: list[str], foldable: bool, number: str, weight: int, manufacturer: str, color: str, five_G_enabled: bool):
        super().__init__(number, weight, manufacturer, color, five_G_enabled)
        self.apps = apps
        self.foldable = foldable
        
my_phone = SmartPhone(["Candy Crush", "Google Maps"], 
                        False, "07707070707", 400, "Apple", "Green", True)

print(my_phone.__dict__)