from abc import ABC, abstractmethod

from model import Item


class AbstractItemRepository(ABC):
    @abstractmethod
    def add(self, item: Item):
        raise NotImplementedError

    @abstractmethod
    def get(self, id: int):
        raise NotImplementedError
