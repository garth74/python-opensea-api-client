import json
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.order_input_components import OrderInputComponents


T = TypeVar("T", bound="OrderInputWithProtocol")


@_attrs_define
class OrderInputWithProtocol:
    """
    Attributes:
        parameters (OrderInputComponents):
        signature (str): Signature of the signed type data represented by the parameters field.
        protocol_address (str): Exchange contract address. Must be one of ['0x00000000000000adc04c56bf30ac9d3c0aaf14dc']
    """

    parameters: "OrderInputComponents"
    signature: str
    protocol_address: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        parameters = self.parameters.to_dict()

        signature = self.signature

        protocol_address = self.protocol_address

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "parameters": parameters,
                "signature": signature,
                "protocol_address": protocol_address,
            }
        )

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        parameters = (None, json.dumps(self.parameters.to_dict()).encode(), "application/json")

        signature = (None, str(self.signature).encode(), "text/plain")

        protocol_address = (None, str(self.protocol_address).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "parameters": parameters,
                "signature": signature,
                "protocol_address": protocol_address,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.order_input_components import OrderInputComponents

        d = src_dict.copy()
        parameters = OrderInputComponents.from_dict(d.pop("parameters"))

        signature = d.pop("signature")

        protocol_address = d.pop("protocol_address")

        order_input_with_protocol = cls(
            parameters=parameters,
            signature=signature,
            protocol_address=protocol_address,
        )

        order_input_with_protocol.additional_properties = d
        return order_input_with_protocol

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
