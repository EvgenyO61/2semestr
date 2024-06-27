#Создайте класс "Человек" с атрибутами "имя", "возраст" и "пол". Напишите метод,
#который выводит информацию о человеке в формате "Имя: имя, Возраст: возраст,
#Пол: пол".

#Создание базового класса "Животное" и его наследование для создания классов
#"Собака" и "Кошка". В классе "Животное" будут общие методы, такие как "дышать"
#и "питаться", а классы-наследники будут иметь свои уникальные методы и свойства,
#такие как "гавкать" и "мурлыкать".

#Для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют
#сохранять информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно.
#Использовать модуль pickle для сериализации и десериализации объектов Python в
#бинарном формате.

import pickle

# Блок 1 (Задача 1)
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_info(self):
        print(f"Имя: {self.name}, Возраст: {self.age}, Пол: {self.gender}")


# Блок 2 (Задача 2)
class Animal:
    def breathe(self):
        print("Дышит")

    def eat(self):
        print("Питается")


class Dog(Animal):
    def bark(self):
        print("Гавкает")


class Cat(Animal):
    def purr(self):
        print("Мурлычет")


# Блок 3 (Задача 3)
def save_def(filename, *args):
    with open(filename, 'wb') as file:
        pickle.dump(args, file)


def load_def(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)


person1 = Person("Максим", 25, "Мужской")
person2 = Person("Татьяна", 30, "Женский")
dog = Dog()
cat = Cat()

save_def("data.pkl", person1, person2, dog, cat)

loaded_objects = load_def("data.pkl")

for obj in loaded_objects:
    if isinstance(obj, Person):
        obj.display_info()
    elif isinstance(obj, Dog):
        obj.breathe()
        obj.eat()
        obj.bark()
    elif isinstance(obj, Cat):
        obj.breathe()
        obj.eat()
        obj.purr()