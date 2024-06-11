import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.social_media_account_model import SocialMediaAccountModel


T = TypeVar("T", bound="DetailedAccountDataModel")


@_attrs_define
class DetailedAccountDataModel:
    """
    Attributes:
        address (Union[Unset, str]): The unique public blockchain identifier for the wallet. Default: ''.
        username (Union[Unset, str]): The OpenSea account's username. Default: ''.
        profile_image_url (Union[Unset, str]): The OpenSea account's image url. Default: ''.
        banner_image_url (Union[Unset, str]): The OpenSea account's banner url. Default: ''.
        website (Union[Unset, str]): Personal website for the OpenSea user. Default: ''.
        social_media_accounts (Union[Unset, List['SocialMediaAccountModel']]):
        bio (Union[Unset, str]): The OpenSea account's bio. Default: ''.
        joined_date (Union[Unset, datetime.date]): Date the account was first added to OpenSea.
    """

    address: Union[Unset, str] = ""
    username: Union[Unset, str] = ""
    profile_image_url: Union[Unset, str] = ""
    banner_image_url: Union[Unset, str] = ""
    website: Union[Unset, str] = ""
    social_media_accounts: Union[Unset, List["SocialMediaAccountModel"]] = UNSET
    bio: Union[Unset, str] = ""
    joined_date: Union[Unset, datetime.date] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        address = self.address

        username = self.username

        profile_image_url = self.profile_image_url

        banner_image_url = self.banner_image_url

        website = self.website

        social_media_accounts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.social_media_accounts, Unset):
            social_media_accounts = []
            for social_media_accounts_item_data in self.social_media_accounts:
                social_media_accounts_item = social_media_accounts_item_data.to_dict()
                social_media_accounts.append(social_media_accounts_item)

        bio = self.bio

        joined_date: Union[Unset, str] = UNSET
        if not isinstance(self.joined_date, Unset):
            joined_date = self.joined_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if username is not UNSET:
            field_dict["username"] = username
        if profile_image_url is not UNSET:
            field_dict["profile_image_url"] = profile_image_url
        if banner_image_url is not UNSET:
            field_dict["banner_image_url"] = banner_image_url
        if website is not UNSET:
            field_dict["website"] = website
        if social_media_accounts is not UNSET:
            field_dict["social_media_accounts"] = social_media_accounts
        if bio is not UNSET:
            field_dict["bio"] = bio
        if joined_date is not UNSET:
            field_dict["joined_date"] = joined_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.social_media_account_model import SocialMediaAccountModel

        d = src_dict.copy()
        address = d.pop("address", UNSET)

        username = d.pop("username", UNSET)

        profile_image_url = d.pop("profile_image_url", UNSET)

        banner_image_url = d.pop("banner_image_url", UNSET)

        website = d.pop("website", UNSET)

        social_media_accounts = []
        _social_media_accounts = d.pop("social_media_accounts", UNSET)
        for social_media_accounts_item_data in _social_media_accounts or []:
            social_media_accounts_item = SocialMediaAccountModel.from_dict(social_media_accounts_item_data)

            social_media_accounts.append(social_media_accounts_item)

        bio = d.pop("bio", UNSET)

        _joined_date = d.pop("joined_date", UNSET)
        joined_date: Union[Unset, datetime.date]
        if isinstance(_joined_date, Unset):
            joined_date = UNSET
        else:
            joined_date = isoparse(_joined_date).date()

        detailed_account_data_model = cls(
            address=address,
            username=username,
            profile_image_url=profile_image_url,
            banner_image_url=banner_image_url,
            website=website,
            social_media_accounts=social_media_accounts,
            bio=bio,
            joined_date=joined_date,
        )

        detailed_account_data_model.additional_properties = d
        return detailed_account_data_model

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
