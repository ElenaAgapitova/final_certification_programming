from tabulate import tabulate

from model.pack_animals import Horses, Camels, Donkeys
from model.pets import Cats, Dogs, Hamsters


class RegistryAnimals:
    def __init__(self):
        self.__log_registry = []

    def get_log_registry(self):
        return self.__log_registry

    def number_of_animals(self):
        return len(self.__log_registry)

    def add_cat(self, name, command, birth_date):
        cat = Cats(name, command, birth_date)
        self.__log_registry.append(cat)

    def add_dog(self, name, command, birth_date):
        dog = Dogs(name, command, birth_date)
        self.__log_registry.append(dog)

    def add_hamster(self, name, command, birth_date):
        hamster = Hamsters(name, command, birth_date)
        self.__log_registry.append(hamster)

    def add_horse(self, name, command, birth_date):
        horse = Horses(name, command, birth_date)
        self.__log_registry.append(horse)

    def add_camel(self, name, command, birth_date):
        camel = Camels(name, command, birth_date)
        self.__log_registry.append(camel)

    def add_donkey(self, name, command, birth_date):
        donkey = Donkeys(name, command, birth_date)
        self.__log_registry.append(donkey)

    @property
    def tabl_registry(self):
        """
        Формирует представление реестра в виде таблицы.
        :return: список всех животных в виде таблицы
        """
        headers = ['№', 'Тип животного', 'Вид животного', 'Имя',
                   'Список команд', 'Дата рождения']
        tabl = [[i, animal.get_type_animals(),
                 animal.get_kind_animals(), animal.get_name(),
                 animal.get_command(), animal.get_birth_date()]
                for i, animal in enumerate(self.__log_registry, start=1)]
        return tabulate(tabl, headers=headers, tablefmt="fancy_grid", stralign='center')
