from Data.dbsqlite_manager import DataManager


class Presenter:
    """
    Presenter для паттерна MVP.
    Принимает на вход экземпляры View и Notebook и связывает их между собой.
    """

    def __init__(self, view, log_registry, path: str):
        self.__view = view
        self.__log_registry = log_registry
        self.__view.set_presenter(self)
        self.__data = DataManager(path)

    def read_db(self):
        self.__data.read_db(self.__log_registry)

    def get_tabl_registry(self):
        return self.__log_registry.tabl_registry

    def get_log_registry(self):
        return self.__log_registry

    def all_kinds_pets(self):
        return self.__log_registry.list_kind_pets()

    def all_kinds_pack(self):
        return self.__log_registry.list_kind_pack()

    def add_cat(self, name, command, birth_date):
        self.__log_registry.add_cat(name, command, birth_date)

    def add_dog(self, name, command, birth_date):
        self.__log_registry.add_dog(name, command, birth_date)

    def add_hamster(self, name, command, birth_date):
        self.__log_registry.add_hamster(name, command, birth_date)

    def add_horse(self, name, command, birth_date):
        self.__log_registry.add_horse(name, command, birth_date)

    def add_camel(self, name, command, birth_date):
        self.__log_registry.add_camel(name, command, birth_date)

    def add_donkey(self, name, command, birth_date):
        self.__log_registry.add_donkey(name, command, birth_date)

    def remove(self):
        self.__log_registry.remove()
