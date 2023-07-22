from model.class_pets import Pets


class Cats(Pets):
    def __init__(self, name, command, birth_date):
        super().__init__(kind_animals="кошка")
        self.__name = name
        self.__command = command
        self.__birth_date = birth_date

    def get_command(self):
        return self.__command

    def add_command(self, new_commands):
        self.__command = self.__command + ', ' + new_commands

    def get_name(self):
        return self.__name

    def get_birth_date(self):
        return self.__birth_date


class Dogs(Pets):
    def __init__(self, name, command, birth_date):
        super().__init__(kind_animals="собака")
        self.__name = name
        self.__command = command
        self.__birth_date = birth_date

    def get_command(self):
        return self.__command

    def add_command(self, new_commands):
        self.__command = self.__command + ', ' + new_commands

    def get_name(self):
        return self.__name

    def get_birth_date(self):
        return self.__birth_date


class Hamsters(Pets):
    def __init__(self, name, command, birth_date):
        super().__init__(kind_animals="хомяк")
        self.__name = name
        self.__command = command
        self.__birth_date = birth_date

    def get_command(self):
        return self.__command

    def add_command(self, new_commands):
        self.__command = self.__command + ', ' + new_commands

    def get_name(self):
        return self.__name

    def get_birth_date(self):
        return self.__birth_date
