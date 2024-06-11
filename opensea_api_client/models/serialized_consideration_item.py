from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.item_type import ItemType

T = TypeVar("T", bound="SerializedConsiderationItem")


@_attrs_define
class SerializedConsiderationItem:
    """
    Attributes:
        item_type (ItemType): 0 - Native - Ether (or other native token for the given chain)
            1 - ERC20
            2 - ERC721
            3 - ERC1155
            4 - ERC721 with criteria
            5 - ERC1155 with criteria
        token (str): The item's token contract (with the null address used for native tokens)
        identifier_or_criteria (str): The ERC721 or ERC1155 token identifier or, in the case of a criteria-based item
            type, a merkle root composed of the valid set of token identifiers for the item. This value will be ignored for
            Ether and ERC20 item types, and can optionally be zero for criteria-based item types to allow for any
            identifier.
        start_amount (str): The amount of the token in question that will be required should the order be fulfilled.
        end_amount (str): When endAmount differs from `startAmount`, the realized amount is calculated linearly based on
            the time elapsed since the order became active.
        recipient (str): The address which will receive the consideration item when the order is executed.
    """

    item_type: ItemType
    token: str
    identifier_or_criteria: str
    start_amount: str
    end_amount: str
    recipient: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        item_type = self.item_type.value

        token = self.token

        identifier_or_criteria = self.identifier_or_criteria

        start_amount = self.start_amount

        end_amount = self.end_amount

        recipient = self.recipient

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "itemType": item_type,
                "token": token,
                "identifierOrCriteria": identifier_or_criteria,
                "startAmount": start_amount,
                "endAmount": end_amount,
                "recipient": recipient,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        item_type = ItemType(d.pop("itemType"))

        token = d.pop("token")

        identifier_or_criteria = d.pop("identifierOrCriteria")

        start_amount = d.pop("startAmount")

        end_amount = d.pop("endAmount")

        recipient = d.pop("recipient")

        serialized_consideration_item = cls(
            item_type=item_type,
            token=token,
            identifier_or_criteria=identifier_or_criteria,
            start_amount=start_amount,
            end_amount=end_amount,
            recipient=recipient,
        )

        serialized_consideration_item.additional_properties = d
        return serialized_consideration_item

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
