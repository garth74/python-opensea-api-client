from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.created_at_enum import CreatedAtEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="NftModel")


@_attrs_define
class NftModel:
    """
    Attributes:
        identifier (str): The NFT's unique identifier within the smart contract (also referred to as token_id)
        collection (str): Collection slug. A unique string to identify a collection on OpenSea
        contract (str): The unique public blockchain identifier for the contract
        token_standard (str): ERC standard of the token (erc721, erc1155)
        name (str): Name of the NFT
        description (str): Description of the NFT
        updated_at (str): Last time that the NFT's metadata was updated by OpenSea
        is_disabled (bool): If the item is currently able to be bought or sold using OpenSea
        is_nsfw (bool): If the item is currently classified as 'Not Safe for Work' by OpenSea
        image_url (Union[Unset, str]): Link to the image associated with the NFT Default: ''.
        metadata_url (Union[Unset, str]): Link to the offchain metadata store Default: ''.
        created_at (Union[Unset, CreatedAtEnum]):  Default: CreatedAtEnum.VALUE_0.
    """

    identifier: str
    collection: str
    contract: str
    token_standard: str
    name: str
    description: str
    updated_at: str
    is_disabled: bool
    is_nsfw: bool
    image_url: Union[Unset, str] = ""
    metadata_url: Union[Unset, str] = ""
    created_at: Union[Unset, CreatedAtEnum] = CreatedAtEnum.VALUE_0
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        identifier = self.identifier

        collection = self.collection

        contract = self.contract

        token_standard = self.token_standard

        name = self.name

        description = self.description

        updated_at = self.updated_at

        is_disabled = self.is_disabled

        is_nsfw = self.is_nsfw

        image_url = self.image_url

        metadata_url = self.metadata_url

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "identifier": identifier,
                "collection": collection,
                "contract": contract,
                "token_standard": token_standard,
                "name": name,
                "description": description,
                "updated_at": updated_at,
                "is_disabled": is_disabled,
                "is_nsfw": is_nsfw,
            }
        )
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if metadata_url is not UNSET:
            field_dict["metadata_url"] = metadata_url
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        identifier = d.pop("identifier")

        collection = d.pop("collection")

        contract = d.pop("contract")

        token_standard = d.pop("token_standard")

        name = d.pop("name")

        description = d.pop("description")

        updated_at = d.pop("updated_at")

        is_disabled = d.pop("is_disabled")

        is_nsfw = d.pop("is_nsfw")

        image_url = d.pop("image_url", UNSET)

        metadata_url = d.pop("metadata_url", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, CreatedAtEnum]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = CreatedAtEnum(_created_at)

        nft_model = cls(
            identifier=identifier,
            collection=collection,
            contract=contract,
            token_standard=token_standard,
            name=name,
            description=description,
            updated_at=updated_at,
            is_disabled=is_disabled,
            is_nsfw=is_nsfw,
            image_url=image_url,
            metadata_url=metadata_url,
            created_at=created_at,
        )

        nft_model.additional_properties = d
        return nft_model

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
