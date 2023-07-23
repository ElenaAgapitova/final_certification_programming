from model.registry_animals import RegistryAnimals
from presenter.presenter import Presenter
from view.console import Console

if __name__ == '__main__':
    registry = RegistryAnimals()
    view = Console()
    presenter = Presenter(view, registry, 'human_friends2.db')
    view.start()



