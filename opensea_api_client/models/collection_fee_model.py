from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CollectionFeeModel")


@_attrs_define
class CollectionFeeModel:
    """
    Attributes:
        fee (float): Percentage of the sale price that is paid to the recipient
        recipient (str): The unique public blockchain identifier, address, for the recipient
        required (Union[Unset, bool]): If the fee is required for the collection Default: False.
    """

    fee: float
    recipient: str
    required: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        fee = self.fee

        recipient = self.recipient

        required = self.required

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fee": fee,
                "recipient": recipient,
            }
        )
        if required is not UNSET:
            field_dict["required"] = required

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        fee = d.pop("fee")

        recipient = d.pop("recipient")

        required = d.pop("required", UNSET)

        collection_fee_model = cls(
            fee=fee,
            recipient=recipient,
            required=required,
        )

        collection_fee_model.additional_properties = d
        return collection_fee_model

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
