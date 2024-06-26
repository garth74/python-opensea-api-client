from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.category_type import CategoryType

T = TypeVar("T", bound="GetTraitResponseCategories")


@_attrs_define
class GetTraitResponseCategories:
    """List of trait categories, e.g. Background, in the collection and their type, e.g. string"""

    additional_properties: Dict[str, CategoryType] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        get_trait_response_categories = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = CategoryType(prop_dict)

            additional_properties[prop_name] = additional_property

        get_trait_response_categories.additional_properties = additional_properties
        return get_trait_response_categories

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> CategoryType:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: CategoryType) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
