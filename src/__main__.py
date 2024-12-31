""" Entry point of the application """

from model import Item
from fileitemrepository import FileItemRepository

# ToDo implement click tasks: add {task},  show, done {id}


def run_app():
    print(f"First step")

    item1 = Item(task="Do something")
    itemrepository = FileItemRepository(r"./data/output/todoitems.json")
    itemrepository.add(item1)

    item = itemrepository.get(itemrepository.find_last_id() - 1)
    if type(item) == Item:
        if item.end_date == None:
            item.done()
        else:
            item.undone()
        print(item.model_dump_json())

    itemrepository.save_data()
    print("Finished")


if __name__ == "__main__":
    run_app()
