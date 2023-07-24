from Data.dbsqlite_manager import DataManager


class Presenter:

    def __init__(self, view, log_registry, path: str):
        self.__view = view
        self.__log_registry = log_registry
        self.__view.set_presenter(self)
        self.__data = DataManager(path)

    def read_db(self):
        return self.__data.read_db(self.__log_registry)

    def get_tabl_registry(self):
        return self.__log_registry.tabl_registry

    def all_kinds_pets(self):
        return self.__log_registry.list_kind_pets()

    def all_kinds_pack(self):
        return self.__log_registry.list_kind_pack()

    def add_animal(self, kind, name, command, birth_date):
        self.__log_registry.add_animal(kind, name, command, birth_date)

    def save_animal_into_bd(self, type_id, kind, name, command, birth_date):
        return self.__data.save_animal(type_id, kind, name, command, birth_date)

    def find_animal(self, index):
        return self.__log_registry.find_animal(index)

    def get_command(self, index):
        return self.__log_registry.get_command(index)

    def add_command(self, index, commands):
        self.__log_registry.add_command(index, commands)

    def size_registry(self):
        return self.__log_registry.number_of_animals()

    def save_command(self, index):
        return self.__data.save_command(index, self.__log_registry)
