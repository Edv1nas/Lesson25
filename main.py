class Person:
    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self.__age = age

    def get_name(self):
        return self._name

    def get_age(self):
        return self.__age


me = Person(name="Labas", age=18)

print(me.get_age())
print(me.get_name())
