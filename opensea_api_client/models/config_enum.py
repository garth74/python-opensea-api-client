from enum import Enum


class ConfigEnum(str, Enum):
    AFFILIATE = "affiliate"
    AFFILIATE_BLACKLISTED = "affiliate_blacklisted"
    AFFILIATE_PARTNER = "affiliate_partner"
    AFFILIATE_REQUESTED = "affiliate_requested"
    EMPLOYEE = "employee"
    MODERATOR = "moderator"
    STAFF = "staff"
    VERIFIED = "verified"

    def __str__(self) -> str:
        return str(self.value)
