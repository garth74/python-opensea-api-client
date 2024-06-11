from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.collection import Collection
    from ..models.contract import Contract
    from ..models.trait import Trait


T = TypeVar("T", bound="Criteria")


@_attrs_define
class Criteria:
    """
    Attributes:
        collection (Collection):
        contract (Contract):
        trait (Union[Unset, Trait]):
        encoded_token_ids (Union[Unset, str]): Represents a list of token ids which can be used to fulfill the criteria
            offer. When decoded using the provided SDK function, developers can now see a list of all tokens that could be
            used to fulfill the offer.
    """

    collection: "Collection"
    contract: "Contract"
    trait: Union[Unset, "Trait"] = UNSET
    encoded_token_ids: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        collection = self.collection.to_dict()

        contract = self.contract.to_dict()

        trait: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.trait, Unset):
            trait = self.trait.to_dict()

        encoded_token_ids = self.encoded_token_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collection": collection,
                "contract": contract,
            }
        )
        if trait is not UNSET:
            field_dict["trait"] = trait
        if encoded_token_ids is not UNSET:
            field_dict["encoded_token_ids"] = encoded_token_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.collection import Collection
        from ..models.contract import Contract
        from ..models.trait import Trait

        d = src_dict.copy()
        collection = Collection.from_dict(d.pop("collection"))

        contract = Contract.from_dict(d.pop("contract"))

        _trait = d.pop("trait", UNSET)
        trait: Union[Unset, Trait]
        if isinstance(_trait, Unset):
            trait = UNSET
        else:
            trait = Trait.from_dict(_trait)

        encoded_token_ids = d.pop("encoded_token_ids", UNSET)

        criteria = cls(
            collection=collection,
            contract=contract,
            trait=trait,
            encoded_token_ids=encoded_token_ids,
        )

        criteria.additional_properties = d
        return criteria

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
