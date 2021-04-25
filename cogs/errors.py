from typing import Optional, Union


class GuildNotFound(ValueError):

    def __init__(self, name: Optional[Union[str, int]] = None, guild_id: Optional[int] = None):
        self.name = name
        self.id = guild_id
        msgs = ["Guild ", "not found"]
        last = 1
        if name is not None:
            msgs = ["".join(msgs[:last]), str(name) + " ", "".join(msgs[last:])]
            last += 1
        if guild_id is not None and type(name) != int:
            msgs = ["".join(msgs[:last]), str(guild_id) + " ", "".join(msgs[last:])]
        super(GuildNotFound, self).__init__("".join(msgs))


__all__ = ["GuildNotFound"]
