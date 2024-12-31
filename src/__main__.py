""" Entry point of the application """

import click

from model import Item
from fileitemrepository import FileItemRepository

# ToDo implement click tasks: add {task},  show, done {id}


@click.command()
@click.option("--add", default="Do something", help="Add a task.")
@click.option("--show", default="All", help="Shows list of tasks (All, Done, Todo).")
@click.option("--done", help="Give task_id and this task will be registered as done.")
def run_app(add, show, done):
    print(f"First step")
    itemrepository = FileItemRepository(r"./data/output/todoitems.json")

    if add != None:
        item = Item(task=add)
        itemrepository.add(item)
        itemrepository.save_data()

    if show != None:
        print(f"ToDo: print{show=}")

    if done != None:
        print(f"ToDo: print{done=}")

    print("Finished")


if __name__ == "__main__":
    run_app()
