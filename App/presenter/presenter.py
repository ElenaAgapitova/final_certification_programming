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
        self.__data.read_cat(self.__log_registry)
        self.__data.read_dog(self.__log_registry)
        self.__data.read_hamster(self.__log_registry)
        self.__data.read_horse(self.__log_registry)
        self.__data.read_camel(self.__log_registry)
        self.__data.read_donkey(self.__log_registry)

    def get_tabl_registry(self):
        return self.__log_registry.tabl_registry

    def get_log_registry(self):
        return self.__log_registry
