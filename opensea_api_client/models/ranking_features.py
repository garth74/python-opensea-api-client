from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RankingFeatures")


@_attrs_define
class RankingFeatures:
    """
    Attributes:
        unique_attribute_count (Union[Unset, int]): Deprecated Field. Default: 0.
    """

    unique_attribute_count: Union[Unset, int] = 0
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unique_attribute_count = self.unique_attribute_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unique_attribute_count is not UNSET:
            field_dict["unique_attribute_count"] = unique_attribute_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        unique_attribute_count = d.pop("unique_attribute_count", UNSET)

        ranking_features = cls(
            unique_attribute_count=unique_attribute_count,
        )

        ranking_features.additional_properties = d
        return ranking_features

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
