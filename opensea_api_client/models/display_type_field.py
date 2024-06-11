from enum import Enum


class DisplayTypeField(str, Enum):
    AUTHOR = "author"
    BOOST_NUMBER = "boost_number"
    BOOST_PERCENTAGE = "boost_percentage"
    DATE = "date"
    NONE = "None"
    NUMBER = "number"

    def __str__(self) -> str:
        return str(self.value)
