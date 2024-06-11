from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.chain_identifier import ChainIdentifier
from ..models.sale_event_model_event_type_enum import SaleEventModelEventTypeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_payment_model import EventPaymentModel


T = TypeVar("T", bound="SaleEventModel")


@_attrs_define
class SaleEventModel:
    """
    Attributes:
        order_hash (str): Order hash for the order which was fulfilled
        chain (ChainIdentifier): OpenSea supported chains.
        protocol_address (str): Exchange contract address which fulfilled the order
        closing_date (int): The Posix timestamp at which the transaction which filled the order occurred
        quantity (int): Number of assets transferred
        maker (str): Maker of the order
        taker (str): Taker of the order
        payment (EventPaymentModel):
        transaction (str): Transaction hash for the order fulfillment
        event_type (Union[Unset, SaleEventModelEventTypeEnum]):  Default: SaleEventModelEventTypeEnum.SALE.
    """

    order_hash: str
    chain: ChainIdentifier
    protocol_address: str
    closing_date: int
    quantity: int
    maker: str
    taker: str
    payment: "EventPaymentModel"
    transaction: str
    event_type: Union[Unset, SaleEventModelEventTypeEnum] = SaleEventModelEventTypeEnum.SALE
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        order_hash = self.order_hash

        chain = self.chain.value

        protocol_address = self.protocol_address

        closing_date = self.closing_date

        quantity = self.quantity

        maker = self.maker

        taker = self.taker

        payment = self.payment.to_dict()

        transaction = self.transaction

        event_type: Union[Unset, str] = UNSET
        if not isinstance(self.event_type, Unset):
            event_type = self.event_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "order_hash": order_hash,
                "chain": chain,
                "protocol_address": protocol_address,
                "closing_date": closing_date,
                "quantity": quantity,
                "maker": maker,
                "taker": taker,
                "payment": payment,
                "transaction": transaction,
            }
        )
        if event_type is not UNSET:
            field_dict["event_type"] = event_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.event_payment_model import EventPaymentModel

        d = src_dict.copy()
        order_hash = d.pop("order_hash")

        chain = ChainIdentifier(d.pop("chain"))

        protocol_address = d.pop("protocol_address")

        closing_date = d.pop("closing_date")

        quantity = d.pop("quantity")

        maker = d.pop("maker")

        taker = d.pop("taker")

        payment = EventPaymentModel.from_dict(d.pop("payment"))

        transaction = d.pop("transaction")

        _event_type = d.pop("event_type", UNSET)
        event_type: Union[Unset, SaleEventModelEventTypeEnum]
        if isinstance(_event_type, Unset):
            event_type = UNSET
        else:
            event_type = SaleEventModelEventTypeEnum(_event_type)

        sale_event_model = cls(
            order_hash=order_hash,
            chain=chain,
            protocol_address=protocol_address,
            closing_date=closing_date,
            quantity=quantity,
            maker=maker,
            taker=taker,
            payment=payment,
            transaction=transaction,
            event_type=event_type,
        )

        sale_event_model.additional_properties = d
        return sale_event_model

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
