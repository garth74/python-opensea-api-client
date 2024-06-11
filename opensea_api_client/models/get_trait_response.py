from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_trait_response_categories import GetTraitResponseCategories
    from ..models.get_trait_response_counts import GetTraitResponseCounts


T = TypeVar("T", bound="GetTraitResponse")


@_attrs_define
class GetTraitResponse:
    """
    Attributes:
        categories (Union[Unset, GetTraitResponseCategories]): List of trait categories, e.g. Background, in the
            collection and their type, e.g. string
        counts (Union[Unset, GetTraitResponseCounts]): If the category type is STRING, the dict will contain each trait
            value and its count. Otherwise, the dict will contain the min and max value seen in the collection
    """

    categories: Union[Unset, "GetTraitResponseCategories"] = UNSET
    counts: Union[Unset, "GetTraitResponseCounts"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        categories: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.categories, Unset):
            categories = self.categories.to_dict()

        counts: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.counts, Unset):
            counts = self.counts.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if categories is not UNSET:
            field_dict["categories"] = categories
        if counts is not UNSET:
            field_dict["counts"] = counts

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_trait_response_categories import GetTraitResponseCategories
        from ..models.get_trait_response_counts import GetTraitResponseCounts

        d = src_dict.copy()
        _categories = d.pop("categories", UNSET)
        categories: Union[Unset, GetTraitResponseCategories]
        if isinstance(_categories, Unset):
            categories = UNSET
        else:
            categories = GetTraitResponseCategories.from_dict(_categories)

        _counts = d.pop("counts", UNSET)
        counts: Union[Unset, GetTraitResponseCounts]
        if isinstance(_counts, Unset):
            counts = UNSET
        else:
            counts = GetTraitResponseCounts.from_dict(_counts)

        get_trait_response = cls(
            categories=categories,
            counts=counts,
        )

        get_trait_response.additional_properties = d
        return get_trait_response

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
