from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.safelist_request_status import SafelistRequestStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.collection_contract_model import CollectionContractModel
    from ..models.collection_fee_model import CollectionFeeModel


T = TypeVar("T", bound="DetailedCollectionModel")


@_attrs_define
class DetailedCollectionModel:
    """
    Attributes:
        collection (str): Collection slug. A unique string to identify a collection on OpenSea
        name (str): Name of the collection
        owner (str): The unique public blockchain identifier, address, for the owner wallet.
        safelist_status (SafelistRequestStatus): Status of the collection verification requests.
        category (str): Category of the collection (e.g. PFPs, Memberships, Art)
        is_disabled (bool): If the collection is currently able to be bought or sold using OpenSea
        is_nsfw (bool): If the collection is currently classified as 'Not Safe for Work' by OpenSea
        trait_offers_enabled (bool): If trait offers are currently being accepted for the collection
        opensea_url (str): OpenSea Link to collection
        contracts (List['CollectionContractModel']):
        editors (List[str]): List of editor addresses for the collection
        fees (List['CollectionFeeModel']): List of fees for the collection including creator earnings and OpenSea fees
        description (Union[Unset, str]): Description of the collection Default: ''.
        project_url (Union[Unset, str]): External URL for the collection's website Default: ''.
        wiki_url (Union[Unset, str]): External URL for the collection's wiki Default: ''.
        discord_url (Union[Unset, str]): External URL for the collection's Discord server Default: ''.
        telegram_url (Union[Unset, str]): External URL for the collection's Telegram group Default: ''.
        twitter_username (Union[Unset, str]): Username for the collection's Twitter account Default: ''.
        instagram_username (Union[Unset, str]): Username for the collection's Instagram account Default: ''.
    """

    collection: str
    name: str
    owner: str
    safelist_status: SafelistRequestStatus
    category: str
    is_disabled: bool
    is_nsfw: bool
    trait_offers_enabled: bool
    opensea_url: str
    contracts: List["CollectionContractModel"]
    editors: List[str]
    fees: List["CollectionFeeModel"]
    description: Union[Unset, str] = ""
    project_url: Union[Unset, str] = ""
    wiki_url: Union[Unset, str] = ""
    discord_url: Union[Unset, str] = ""
    telegram_url: Union[Unset, str] = ""
    twitter_username: Union[Unset, str] = ""
    instagram_username: Union[Unset, str] = ""
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        collection = self.collection

        name = self.name

        owner = self.owner

        safelist_status = self.safelist_status.value

        category = self.category

        is_disabled = self.is_disabled

        is_nsfw = self.is_nsfw

        trait_offers_enabled = self.trait_offers_enabled

        opensea_url = self.opensea_url

        contracts = []
        for contracts_item_data in self.contracts:
            contracts_item = contracts_item_data.to_dict()
            contracts.append(contracts_item)

        editors = self.editors

        fees = []
        for fees_item_data in self.fees:
            fees_item = fees_item_data.to_dict()
            fees.append(fees_item)

        description = self.description

        project_url = self.project_url

        wiki_url = self.wiki_url

        discord_url = self.discord_url

        telegram_url = self.telegram_url

        twitter_username = self.twitter_username

        instagram_username = self.instagram_username

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collection": collection,
                "name": name,
                "owner": owner,
                "safelist_status": safelist_status,
                "category": category,
                "is_disabled": is_disabled,
                "is_nsfw": is_nsfw,
                "trait_offers_enabled": trait_offers_enabled,
                "opensea_url": opensea_url,
                "contracts": contracts,
                "editors": editors,
                "fees": fees,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if project_url is not UNSET:
            field_dict["project_url"] = project_url
        if wiki_url is not UNSET:
            field_dict["wiki_url"] = wiki_url
        if discord_url is not UNSET:
            field_dict["discord_url"] = discord_url
        if telegram_url is not UNSET:
            field_dict["telegram_url"] = telegram_url
        if twitter_username is not UNSET:
            field_dict["twitter_username"] = twitter_username
        if instagram_username is not UNSET:
            field_dict["instagram_username"] = instagram_username

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.collection_contract_model import CollectionContractModel
        from ..models.collection_fee_model import CollectionFeeModel

        d = src_dict.copy()
        collection = d.pop("collection")

        name = d.pop("name")

        owner = d.pop("owner")

        safelist_status = SafelistRequestStatus(d.pop("safelist_status"))

        category = d.pop("category")

        is_disabled = d.pop("is_disabled")

        is_nsfw = d.pop("is_nsfw")

        trait_offers_enabled = d.pop("trait_offers_enabled")

        opensea_url = d.pop("opensea_url")

        contracts = []
        _contracts = d.pop("contracts")
        for contracts_item_data in _contracts:
            contracts_item = CollectionContractModel.from_dict(contracts_item_data)

            contracts.append(contracts_item)

        editors = cast(List[str], d.pop("editors"))

        fees = []
        _fees = d.pop("fees")
        for fees_item_data in _fees:
            fees_item = CollectionFeeModel.from_dict(fees_item_data)

            fees.append(fees_item)

        description = d.pop("description", UNSET)

        project_url = d.pop("project_url", UNSET)

        wiki_url = d.pop("wiki_url", UNSET)

        discord_url = d.pop("discord_url", UNSET)

        telegram_url = d.pop("telegram_url", UNSET)

        twitter_username = d.pop("twitter_username", UNSET)

        instagram_username = d.pop("instagram_username", UNSET)

        detailed_collection_model = cls(
            collection=collection,
            name=name,
            owner=owner,
            safelist_status=safelist_status,
            category=category,
            is_disabled=is_disabled,
            is_nsfw=is_nsfw,
            trait_offers_enabled=trait_offers_enabled,
            opensea_url=opensea_url,
            contracts=contracts,
            editors=editors,
            fees=fees,
            description=description,
            project_url=project_url,
            wiki_url=wiki_url,
            discord_url=discord_url,
            telegram_url=telegram_url,
            twitter_username=twitter_username,
            instagram_username=instagram_username,
        )

        detailed_collection_model.additional_properties = d
        return detailed_collection_model

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
