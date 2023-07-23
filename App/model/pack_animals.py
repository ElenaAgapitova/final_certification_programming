from model.class_pack import PackAnimals


class Horses(PackAnimals):
    def __init__(self, name, command, birth_date):
        super().__init__(kind_animals="лошадь")
        self.__name = name
        self.__command = command
        self.__birth_date = birth_date

    def get_command(self):
        return self.__command

    def add_command(self, new_commands):
        if self.__command == '' or self.__command == 'не обучено':
            self.__command = new_commands
        else:
            self.__command = self.__command + ', ' + new_commands

    def get_name(self):
        return self.__name

    def get_birth_date(self):
        return self.__birth_date


class Camels(PackAnimals):
    def __init__(self, name, command, birth_date):
        super().__init__(kind_animals="верблюд")
        self.__name = name
        self.__command = command
        self.__birth_date = birth_date

    def get_command(self):
        return self.__command

    def add_command(self, new_commands):
        if self.__command == '' or self.__command == 'не обучено':
            self.__command = new_commands
        else:
            self.__command = self.__command + ', ' + new_commands

    def get_name(self):
        return self.__name

    def get_birth_date(self):
        return self.__birth_date


class Donkeys(PackAnimals):
    def __init__(self, name, command, birth_date):
        super().__init__(kind_animals="осёл")
        self.__name = name
        self.__command = command
        self.__birth_date = birth_date

    def get_command(self):
        return self.__command

    def add_command(self, new_commands):
        if self.__command == '' or self.__command == 'не обучено':
            self.__command = new_commands
        else:
            self.__command = self.__command + ', ' + new_commands

    def get_name(self):
        return self.__name

    def get_birth_date(self):
        return self.__birth_date
