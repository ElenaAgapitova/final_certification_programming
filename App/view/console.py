from view.abstract_view import View


class Console(View):
    __working = False

    def __init__(self):
        self.presenter = None

    def set_presenter(self, presenter):
        self.presenter = presenter

    def start(self):
        self.__working = True
        self.presenter.read_db()
        while self.__working:
            print('\n========== Главное меню ===========')
            print('\t1. Открыть реестр животных\n'
                  '\t2. Добавить животное в питомник\n'
                  '\t3. Выбрать животное для просмотра команд\n'
                  '\t4. Выход\n')
            user_choice = self.__get_number(4, 'Выберите пункт в меню: ')
            match user_choice:
                case 1:
                    print("\n\t\t\t\t\t\t\t\t\t\t\tРеестр животных питомника")
                    print(self.presenter.get_tabl_registry())
                case 2:
                    self.__add_animals()
                case 3:
                    pass
                case 4:
                    self.__working = False

    def __add_animals(self):
        print('\n========== Типы животных в питомнике ===========')
        print('\t1. Домашние животные\n'
              '\t2. Вьючные животные\n'
              '\t3. Выход (если нет необходимого типа, обратитесь к администратору)')
        user_choice = self.__get_number(3, "Выберите пункт в меню: ")
        match user_choice:
            case 1:
                self.__add_animal(self.presenter.all_kinds_pets())
            case 2:
                self.__add_animal(self.presenter.all_kinds_pack())
            case 3:
                return

    def __add_animal(self, kinds):
        print(f'\nВиды животных в питомнике: {kinds}\n')
        kind = input('Введите вид животного: ').lower()
        if kind in kinds:
            name = input('Введите имя животного: ').capitalize()
            command = input('Введите список команд через запятую, которыми обучено животное. Или введите'
                            ' "не обучен": ')
            birth_date = input('Введите дату рождения животного в формате ГГГГ-ММ-ДД: ')
            if self.__save_animal(kind, name, command, birth_date):
                self.presenter.add_animal(kind, name, command, birth_date)
                print('Запись сохранена и добавлена в базу данных!')
        else:
            print("\nТакого вида в настоящий момент нет в питомнике. Обратитесь к администратору!")
            return

    @staticmethod
    def __get_number(size: int, text: str):
        """Возвращает индекс для списка заметок или меню"""
        while True:
            user_input = input(text)
            if (user_input.isdigit() and
                    1 <= int(user_input) <= size):
                return int(user_input)
            print(f"\nВведите число от 1 до {size}")

    @staticmethod
    def __save_animal(kind, name, command, birth_date):
        print(f'\nВы хотите добавить животное:\n{kind} {name}\nкоманды: {command}\nд.р. {birth_date}')
        user_choice = input('Сохранить изменения?(д/н): ').lower()
        if user_choice in ['да', 'д', 'y', 'yes']:
            return True
        else:
            print('\nЗапись не сохранена!\n')
            return False
