from enum import Enum


class SafelistRequestStatus(str, Enum):
    APPROVED = "approved"
    DISABLED_TOP_TRENDING = "disabled_top_trending"
    NOT_REQUESTED = "not_requested"
    REQUESTED = "requested"
    VERIFIED = "verified"

    def __str__(self) -> str:
        return str(self.value)
