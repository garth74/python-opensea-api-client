from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.config_enum import ConfigEnum

T = TypeVar("T", bound="SimpleAccount")


@_attrs_define
class SimpleAccount:
    """
    Attributes:
        user (Union[None, int]):
        profile_img_url (str): A placeholder image. For the actual profile image, call the Get Account endpoint.
        address (str): The unique blockchain identifier, address, of the account.
        config (ConfigEnum): * `affiliate` - affiliate
            * `affiliate_partner` - affiliate_partner
            * `affiliate_requested` - affiliate_requested
            * `affiliate_blacklisted` - affiliate_blacklisted
            * `verified` - verified
            * `moderator` - moderator
            * `staff` - staff
            * `employee` - employee
    """

    user: Union[None, int]
    profile_img_url: str
    address: str
    config: ConfigEnum
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user: Union[None, int]
        user = self.user

        profile_img_url = self.profile_img_url

        address = self.address

        config = self.config.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user": user,
                "profile_img_url": profile_img_url,
                "address": address,
                "config": config,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_user(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        user = _parse_user(d.pop("user"))

        profile_img_url = d.pop("profile_img_url")

        address = d.pop("address")

        config = ConfigEnum(d.pop("config"))

        simple_account = cls(
            user=user,
            profile_img_url=profile_img_url,
            address=address,
            config=config,
        )

        simple_account.additional_properties = d
        return simple_account

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
