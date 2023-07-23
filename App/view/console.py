from view.abstract_view import View


class Console(View):

    def __init__(self):
        self.presenter = None

    def set_presenter(self, presenter):
        self.presenter = presenter

    def start(self):
        self.presenter.read_db()
        print("\n\t\t\t\t\t\t\t\t\t\t\tРеестр животных питомника")
        print(self.presenter.get_tabl_registry())

