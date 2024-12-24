from abstractitemrepository import AbstractItemRepository
from model import Item
import json


class FileItemRepository(AbstractItemRepository):
    def __init__(self, filename: str):
        self.filename = filename

    def add(self, item: Item):
        item.item_id = self.find_last_id() + 1
        with open(self.filename, "a") as file:
            file.write(item.model_dump_json() + "\n")

    def get(self, id: int):
        data = []
        with open(self.filename, "r") as file:
            for line in file:
                data = json.loads(line)
                if data["item_id"] == id:
                    return Item(**data)
                else:
                    return None

    def find_last_id(self):
        max_id = -1
        with open(self.filename, "r") as file:
            for line in file:
                data = json.loads(line)
                if max_id < data["item_id"]:
                    max_id = data["item_id"]
        return max_id
