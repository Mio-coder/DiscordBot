from abc import ABC, abstractmethod
from json import load, dump
from os import makedirs
from os.path import split
from typing import Union, Dict, Final


def generate(path: str):
    makedirs("/".join(split(path)[:-1]))
    open(path, "a+").close()


data_format: Final = Dict[str, Dict[str, Union[int, str, list]]]


class IdeasClient(ABC):

    def __init__(self, path: str = "bot-data/cogs-data/ideas-data/data.json"):
        self.path = path

    async def add(self, name: str, author_nick: str = "anonymous"):
        data = await self.get()
        data[name] = {
            "vote": 1,
            "author": author_nick,
            "voted_users": [author_nick]
        }
        with open(self.path, "w") as file:
            dump(data, file)

    async def get(self) -> data_format:
        with open(self.path) as file:
            data: data_format = load(file)
        return data

    async def vote(self, name, author_nick):
        data = await self.get()
        if name in data.keys() and author_nick not in data[name]["voted_users"]:
            data[name]["vote"] += 1
            with open(self.path, "w") as file:
                dump(data, file)

    @abstractmethod
    async def delete(self, name, author_nick):
        pass


generate("../../bot-data/cogs-data/ideas-data/data.json")
