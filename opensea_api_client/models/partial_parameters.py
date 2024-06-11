from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.serialized_consideration_item import SerializedConsiderationItem


T = TypeVar("T", bound="PartialParameters")


@_attrs_define
class PartialParameters:
    """
    Attributes:
        consideration (List['SerializedConsiderationItem']): One of the consideration items used when creating criteria
            offers.
        zone (str): Optional secondary account attached the order which can cancel orders. Additionally, when the
            `OrderType` is Restricted, the zone or the offerer are the only entities which can execute the order.
            For open orders, use the zero address.
            For restricted orders, use the signed zone address 0x000000e7ec00e7b300774b00001314b8610022b8
        zone_hash (str): A value that will be supplied to the zone when fulfilling restricted orders that the zone can
            utilize when making a determination on whether to authorize the order. Most often this value will be the zero
            hash 0x0000000000000000000000000000000000000000000000000000000000000000
    """

    consideration: List["SerializedConsiderationItem"]
    zone: str
    zone_hash: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        consideration = []
        for consideration_item_data in self.consideration:
            consideration_item = consideration_item_data.to_dict()
            consideration.append(consideration_item)

        zone = self.zone

        zone_hash = self.zone_hash

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "consideration": consideration,
                "zone": zone,
                "zoneHash": zone_hash,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.serialized_consideration_item import SerializedConsiderationItem

        d = src_dict.copy()
        consideration = []
        _consideration = d.pop("consideration")
        for consideration_item_data in _consideration:
            consideration_item = SerializedConsiderationItem.from_dict(consideration_item_data)

            consideration.append(consideration_item)

        zone = d.pop("zone")

        zone_hash = d.pop("zoneHash")

        partial_parameters = cls(
            consideration=consideration,
            zone=zone,
            zone_hash=zone_hash,
        )

        partial_parameters.additional_properties = d
        return partial_parameters

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
