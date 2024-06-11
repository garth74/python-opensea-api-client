from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.created_at_enum import CreatedAtEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.owner_model import OwnerModel
    from ..models.rarity_data_model import RarityDataModel
    from ..models.trait_model import TraitModel


T = TypeVar("T", bound="DetailedNftModel")


@_attrs_define
class DetailedNftModel:
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
        is_suspicious (bool): If the item has been reported for suspicious activity by OpenSea
        creator (str): The unique public blockchain identifier, wallet address, for the creator
        traits (List['TraitModel']): List of Trait objects. The field will be null if the NFT has more than 50 traits
        owners (List['OwnerModel']): List of Owners. The field will be null if the NFT has more than 50 owners
        rarity (RarityDataModel):
        image_url (Union[Unset, str]): Link to the NFT's original image. This may be an HTTP url, SVG data, or other
            directly embedded data. Default: ''.
        metadata_url (Union[Unset, str]): Link to the offchain metadata store Default: ''.
        created_at (Union[Unset, CreatedAtEnum]):  Default: CreatedAtEnum.VALUE_0.
        animation_url (Union[Unset, str]): Link to the NFT's original animation. Default: ''.
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
    is_suspicious: bool
    creator: str
    traits: List["TraitModel"]
    owners: List["OwnerModel"]
    rarity: "RarityDataModel"
    image_url: Union[Unset, str] = ""
    metadata_url: Union[Unset, str] = ""
    created_at: Union[Unset, CreatedAtEnum] = CreatedAtEnum.VALUE_0
    animation_url: Union[Unset, str] = ""
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

        is_suspicious = self.is_suspicious

        creator = self.creator

        traits = []
        for traits_item_data in self.traits:
            traits_item = traits_item_data.to_dict()
            traits.append(traits_item)

        owners = []
        for owners_item_data in self.owners:
            owners_item = owners_item_data.to_dict()
            owners.append(owners_item)

        rarity = self.rarity.to_dict()

        image_url = self.image_url

        metadata_url = self.metadata_url

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.value

        animation_url = self.animation_url

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
                "is_suspicious": is_suspicious,
                "creator": creator,
                "traits": traits,
                "owners": owners,
                "rarity": rarity,
            }
        )
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if metadata_url is not UNSET:
            field_dict["metadata_url"] = metadata_url
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if animation_url is not UNSET:
            field_dict["animation_url"] = animation_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.owner_model import OwnerModel
        from ..models.rarity_data_model import RarityDataModel
        from ..models.trait_model import TraitModel

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

        is_suspicious = d.pop("is_suspicious")

        creator = d.pop("creator")

        traits = []
        _traits = d.pop("traits")
        for traits_item_data in _traits:
            traits_item = TraitModel.from_dict(traits_item_data)

            traits.append(traits_item)

        owners = []
        _owners = d.pop("owners")
        for owners_item_data in _owners:
            owners_item = OwnerModel.from_dict(owners_item_data)

            owners.append(owners_item)

        rarity = RarityDataModel.from_dict(d.pop("rarity"))

        image_url = d.pop("image_url", UNSET)

        metadata_url = d.pop("metadata_url", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, CreatedAtEnum]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = CreatedAtEnum(_created_at)

        animation_url = d.pop("animation_url", UNSET)

        detailed_nft_model = cls(
            identifier=identifier,
            collection=collection,
            contract=contract,
            token_standard=token_standard,
            name=name,
            description=description,
            updated_at=updated_at,
            is_disabled=is_disabled,
            is_nsfw=is_nsfw,
            is_suspicious=is_suspicious,
            creator=creator,
            traits=traits,
            owners=owners,
            rarity=rarity,
            image_url=image_url,
            metadata_url=metadata_url,
            created_at=created_at,
            animation_url=animation_url,
        )

        detailed_nft_model.additional_properties = d
        return detailed_nft_model

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
