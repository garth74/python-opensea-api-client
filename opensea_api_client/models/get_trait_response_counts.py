from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_trait_response_counts_additional_property import GetTraitResponseCountsAdditionalProperty


T = TypeVar("T", bound="GetTraitResponseCounts")


@_attrs_define
class GetTraitResponseCounts:
    """If the category type is STRING, the dict will contain each trait value and its count. Otherwise, the dict will
    contain the min and max value seen in the collection

    """

    additional_properties: Dict[str, "GetTraitResponseCountsAdditionalProperty"] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_trait_response_counts_additional_property import GetTraitResponseCountsAdditionalProperty

        d = src_dict.copy()
        get_trait_response_counts = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = GetTraitResponseCountsAdditionalProperty.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        get_trait_response_counts.additional_properties = additional_properties
        return get_trait_response_counts

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "GetTraitResponseCountsAdditionalProperty":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "GetTraitResponseCountsAdditionalProperty") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
