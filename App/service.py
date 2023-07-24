from model.registry_animals import RegistryAnimals
from presenter.presenter import Presenter
from view.console import Console


class Service:
    def __init__(self):
        self.registry = RegistryAnimals()
        self.view = Console()
        Presenter(self.view, self.registry, 'human_friends2.db')

    def start(self):
        self.view.start()
