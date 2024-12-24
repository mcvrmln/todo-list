""" Entry point of the application """

from model import Item
from fileitemrepository import FileItemRepository


def run_app():
    print(f"First step")

    item1 = Item(**{"item_id": 1, "task": "Do something"})
    itemrepository = FileItemRepository(r"./data/output/todoitems.json")
    itemrepository.add(item1)

    item = itemrepository.get(1)
    item.done()
    print(item.model_dump_json())
    print("Finished")


if __name__ == "__main__":
    run_app()
