from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.order_input_components import OrderInputComponents


T = TypeVar("T", bound="OrderInput")


@_attrs_define
class OrderInput:
    """
    Attributes:
        parameters (OrderInputComponents):
        signature (str): Signature of the signed type data represented by the parameters field.
    """

    parameters: "OrderInputComponents"
    signature: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        parameters = self.parameters.to_dict()

        signature = self.signature

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "parameters": parameters,
                "signature": signature,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.order_input_components import OrderInputComponents

        d = src_dict.copy()
        parameters = OrderInputComponents.from_dict(d.pop("parameters"))

        signature = d.pop("signature")

        order_input = cls(
            parameters=parameters,
            signature=signature,
        )

        order_input.additional_properties = d
        return order_input

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
