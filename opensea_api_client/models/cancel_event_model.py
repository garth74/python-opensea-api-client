from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cancel_event_model_event_type_enum import CancelEventModelEventTypeEnum
from ..models.chain_identifier import ChainIdentifier
from ..types import UNSET, Unset

T = TypeVar("T", bound="CancelEventModel")


@_attrs_define
class CancelEventModel:
    """
    Attributes:
        order_hash (str): Order hash for the order which was cancelled
        chain (ChainIdentifier): OpenSea supported chains.
        event_type (Union[Unset, CancelEventModelEventTypeEnum]):  Default: CancelEventModelEventTypeEnum.CANCEL.
    """

    order_hash: str
    chain: ChainIdentifier
    event_type: Union[Unset, CancelEventModelEventTypeEnum] = CancelEventModelEventTypeEnum.CANCEL
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        order_hash = self.order_hash

        chain = self.chain.value

        event_type: Union[Unset, str] = UNSET
        if not isinstance(self.event_type, Unset):
            event_type = self.event_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "order_hash": order_hash,
                "chain": chain,
            }
        )
        if event_type is not UNSET:
            field_dict["event_type"] = event_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        order_hash = d.pop("order_hash")

        chain = ChainIdentifier(d.pop("chain"))

        _event_type = d.pop("event_type", UNSET)
        event_type: Union[Unset, CancelEventModelEventTypeEnum]
        if isinstance(_event_type, Unset):
            event_type = UNSET
        else:
            event_type = CancelEventModelEventTypeEnum(_event_type)

        cancel_event_model = cls(
            order_hash=order_hash,
            chain=chain,
            event_type=event_type,
        )

        cancel_event_model.additional_properties = d
        return cancel_event_model

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
