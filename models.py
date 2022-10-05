from enum import Enum, unique
from typing import List


@unique
class Intent(Enum):
    O = "/O"
    Person = "PER"
    Room = "ROOM"
    Building = "BUILD"
    Floor = "FLOOR"
    Ordinal = "ORD"
    Cardinal = "CAR"
    Date = "DATE"
    Time = "TIME"
    Money = "MONEY"
    Event = "EVE"
    Announcement = "ANN"
    CountryCity = "GPE"
    Location = "LOC"
    Organization = "ORG"

    def splitEntity(self, entity: str) -> str:

        my1: str = (entity + " ").replace(" ", "/B-{} ".format(self.value))
        if my1.count(" ") > 1:
            my11 = my1.split(" ", maxsplit=1)
            final = " ".join([my11[0], my11[1].replace("/B-{}".format(self.value), "/I-{}".format(self.value)).strip()])
            return final
        else:
            return my1.strip()
