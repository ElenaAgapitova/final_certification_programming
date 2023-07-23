import sqlite3

from model.pack_animals import Horses, Camels, Donkeys
from model.pets import Cats, Dogs, Hamsters
from model.registry_animals import RegistryAnimals


class DataManager:
    def __init__(self, path: str):
        self.__path = path

    def read_cat(self, log_registry: RegistryAnimals):
        cursor = None
        connect = None
        try:
            connect = sqlite3.connect(self.__path)
            cursor = connect.cursor()
            cursor.execute("SELECT name, command, birth_date FROM cats")
            rows = cursor.fetchall()
            for row in rows:
                cat = Cats(row[0], row[1], row[2])
                log_registry.get_log_registry().append(cat)
        except sqlite3.Error as e:
            print("Ошибка при работе с базой данных:", e)

        finally:
            if cursor:
                cursor.close()
            if connect:
                connect.close()

    def read_dog(self, log_registry: RegistryAnimals):
        cursor = None
        connect = None
        try:
            connect = sqlite3.connect(self.__path)
            cursor = connect.cursor()
            cursor.execute("SELECT name, command, birth_date FROM dogs")
            rows = cursor.fetchall()
            for row in rows:
                dog = Dogs(row[0], row[1], row[2])
                log_registry.get_log_registry().append(dog)
        except sqlite3.Error as e:
            print("Ошибка при работе с базой данных:", e)

        finally:
            if cursor:
                cursor.close()
            if connect:
                connect.close()

    def read_hamster(self, log_registry: RegistryAnimals):
        cursor = None
        connect = None
        try:
            connect = sqlite3.connect(self.__path)
            cursor = connect.cursor()
            cursor.execute("SELECT name, command, birth_date FROM hamsters")
            rows = cursor.fetchall()
            for row in rows:
                hamster = Hamsters(row[0], row[1], row[2])
                log_registry.get_log_registry().append(hamster)
        except sqlite3.Error as e:
            print("Ошибка при работе с базой данных:", e)

        finally:
            if cursor:
                cursor.close()
            if connect:
                connect.close()

    def read_horse(self, log_registry: RegistryAnimals):
        cursor = None
        connect = None
        try:
            connect = sqlite3.connect(self.__path)
            cursor = connect.cursor()
            cursor.execute("SELECT name, command, birth_date FROM horses")
            rows = cursor.fetchall()
            for row in rows:
                horse = Horses(row[0], row[1], row[2])
                log_registry.get_log_registry().append(horse)
        except sqlite3.Error as e:
            print("Ошибка при работе с базой данных:", e)

        finally:
            if cursor:
                cursor.close()
            if connect:
                connect.close()

    def read_camel(self, log_registry: RegistryAnimals):
        cursor = None
        connect = None
        try:
            connect = sqlite3.connect(self.__path)
            cursor = connect.cursor()
            cursor.execute("SELECT name, command, birth_date FROM camels")
            rows = cursor.fetchall()
            for row in rows:
                camel = Camels(row[0], row[1], row[2])
                log_registry.get_log_registry().append(camel)
        except sqlite3.Error as e:
            print("Ошибка при работе с базой данных:", e)

        finally:
            if cursor:
                cursor.close()
            if connect:
                connect.close()

    def read_donkey(self, log_registry: RegistryAnimals):
        cursor = None
        connect = None
        try:
            connect = sqlite3.connect(self.__path)
            cursor = connect.cursor()
            cursor.execute("SELECT name, command, birth_date FROM donkeys")
            rows = cursor.fetchall()
            for row in rows:
                donkey = Donkeys(row[0], row[1], row[2])
                log_registry.get_log_registry().append(donkey)
        except sqlite3.Error as e:
            print("Ошибка при работе с базой данных:", e)

        finally:
            if cursor:
                cursor.close()
            if connect:
                connect.close()


# logs = RegistryAnimals()
# data = DataManager('human_friends2.db')
# data.read_cat(logs)
# data.read_dog(logs)
# data.read_hamster(logs)
# data.read_horse(logs)
# data.read_camel(logs)
# data.read_donkey(logs)
# print(logs.tabl_registry)
