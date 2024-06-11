from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.chain_identifier import ChainIdentifier
from ..models.transfer_event_model_event_type_enum import TransferEventModelEventTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="TransferEventModel")


@_attrs_define
class TransferEventModel:
    """
    Attributes:
        chain (ChainIdentifier): OpenSea supported chains.
        transaction (str): Transaction hash for the transfer
        from_address (str): Address of the sender
        to_address (str): Address of the recipient
        quantity (int): Number of assets transferred
        event_type (Union[Unset, TransferEventModelEventTypeEnum]):  Default: TransferEventModelEventTypeEnum.TRANSFER.
    """

    chain: ChainIdentifier
    transaction: str
    from_address: str
    to_address: str
    quantity: int
    event_type: Union[Unset, TransferEventModelEventTypeEnum] = TransferEventModelEventTypeEnum.TRANSFER
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        chain = self.chain.value

        transaction = self.transaction

        from_address = self.from_address

        to_address = self.to_address

        quantity = self.quantity

        event_type: Union[Unset, str] = UNSET
        if not isinstance(self.event_type, Unset):
            event_type = self.event_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chain": chain,
                "transaction": transaction,
                "from_address": from_address,
                "to_address": to_address,
                "quantity": quantity,
            }
        )
        if event_type is not UNSET:
            field_dict["event_type"] = event_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        chain = ChainIdentifier(d.pop("chain"))

        transaction = d.pop("transaction")

        from_address = d.pop("from_address")

        to_address = d.pop("to_address")

        quantity = d.pop("quantity")

        _event_type = d.pop("event_type", UNSET)
        event_type: Union[Unset, TransferEventModelEventTypeEnum]
        if isinstance(_event_type, Unset):
            event_type = UNSET
        else:
            event_type = TransferEventModelEventTypeEnum(_event_type)

        transfer_event_model = cls(
            chain=chain,
            transaction=transaction,
            from_address=from_address,
            to_address=to_address,
            quantity=quantity,
            event_type=event_type,
        )

        transfer_event_model.additional_properties = d
        return transfer_event_model

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
