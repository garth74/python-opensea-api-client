from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FulfillmentInput")


@_attrs_define
class FulfillmentInput:
    """
    Attributes:
        hash_ (str): Hash of the order to fulfill.
        chain (str):
        protocol_address (Union[Unset, str]): Exchange contract address. Must be one of
            ['0x00000000000000adc04c56bf30ac9d3c0aaf14dc']
    """

    hash_: str
    chain: str
    protocol_address: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hash_ = self.hash_

        chain = self.chain

        protocol_address = self.protocol_address

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hash": hash_,
                "chain": chain,
            }
        )
        if protocol_address is not UNSET:
            field_dict["protocol_address"] = protocol_address

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        hash_ = d.pop("hash")

        chain = d.pop("chain")

        protocol_address = d.pop("protocol_address", UNSET)

        fulfillment_input = cls(
            hash_=hash_,
            chain=chain,
            protocol_address=protocol_address,
        )

        fulfillment_input.additional_properties = d
        return fulfillment_input

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
