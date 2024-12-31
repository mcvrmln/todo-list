from abstractitemrepository import AbstractItemRepository
from model import Item
import json


class FileItemRepository(AbstractItemRepository):
    def __init__(self, filename: str):
        self.filename = filename
        self.data = list()
        self.load_data()

    def load_data(self):
        with open(self.filename, "r") as file:
            for line in file:
                json_data = json.loads(line)
                self.data.append(Item(**json_data))

    def save_data(self):
        with open(self.filename, "w") as file:
            for item in self.data:
                file.write(item.model_dump_json() + "\n")

    def add(self, item: Item):
        item.item_id = self.find_last_id() + 1
        self.data.append(item)

    def get(self, id: int) -> Item | None:
        for item in self.data:
            if item.item_id == id:
                return item
        return None

    def find_last_id(self):
        max_id = -1
        for item in self.data:
            if max_id < item.item_id:
                max_id = item.item_id
        return max_id
