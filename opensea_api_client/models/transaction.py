from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.transaction_input_data import TransactionInputData


T = TypeVar("T", bound="Transaction")


@_attrs_define
class Transaction:
    """
    Attributes:
        function (str): Seaport protocol contract method to use to fulfill the order.
        chain (int): Numeric Chain Identifier.
        to (str): Protocol contract address to use fto fulfill the order.
        value (int): Wei value of the transaction.
        input_data (TransactionInputData): Decoded Call Data.
    """

    function: str
    chain: int
    to: str
    value: int
    input_data: "TransactionInputData"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        function = self.function

        chain = self.chain

        to = self.to

        value = self.value

        input_data = self.input_data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "function": function,
                "chain": chain,
                "to": to,
                "value": value,
                "input_data": input_data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.transaction_input_data import TransactionInputData

        d = src_dict.copy()
        function = d.pop("function")

        chain = d.pop("chain")

        to = d.pop("to")

        value = d.pop("value")

        input_data = TransactionInputData.from_dict(d.pop("input_data"))

        transaction = cls(
            function=function,
            chain=chain,
            to=to,
            value=value,
            input_data=input_data,
        )

        transaction.additional_properties = d
        return transaction

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
