class Counter:
    def __init__(self):
        self.count = 0

    def add(self):
        self.count += 1

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, tb):
        if exc_type:
            # Обнаружено исключение
            print("Работа с объектом типа 'Счетчик' произошла вне ресурсного try")
        elif self.count > 0:
            # Ресурс остался открытым
            print("Ресурс 'Счетчик' остался открытым")


try:
    with Counter() as counter:
        # Работа с объектом типа Счетчик
        print(counter.count)  # Выведет 0
        counter.add()
        print(counter.count)  # Выведет 1
        # Если выполнить завершение работы без вызова add(), будет
        # сгенерировано исключение и сообщение об открытом ресурсе
except Exception:
    pass
