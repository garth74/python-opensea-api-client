from enum import Enum


class CollectionStatsInterval(str, Enum):
    ONE_DAY = "one_day"
    ONE_MONTH = "one_month"
    ONE_WEEK = "one_week"

    def __str__(self) -> str:
        return str(self.value)
