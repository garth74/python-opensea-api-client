from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EventPaymentModel")


@_attrs_define
class EventPaymentModel:
    """
    Attributes:
        quantity (int): Amount of tokens in the order
        token_address (str): The contract address for the ERC20 token
        decimals (int): Returns the number of decimals the token uses - e.g. 8, means to divide the token amount by
            100000000 to get its user representation.
        symbol (str): Returns the symbol of the token, e.g. ETH, WETH, USDC, etc
    """

    quantity: int
    token_address: str
    decimals: int
    symbol: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        quantity = self.quantity

        token_address = self.token_address

        decimals = self.decimals

        symbol = self.symbol

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "quantity": quantity,
                "token_address": token_address,
                "decimals": decimals,
                "symbol": symbol,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        quantity = d.pop("quantity")

        token_address = d.pop("token_address")

        decimals = d.pop("decimals")

        symbol = d.pop("symbol")

        event_payment_model = cls(
            quantity=quantity,
            token_address=token_address,
            decimals=decimals,
            symbol=symbol,
        )

        event_payment_model.additional_properties = d
        return event_payment_model

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
