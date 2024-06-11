import json
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.criteria import Criteria


T = TypeVar("T", bound="BuildOfferInput")


@_attrs_define
class BuildOfferInput:
    """
    Attributes:
        offerer (str): The address which supplies all the items in the offer.
        criteria (Criteria):
        protocol_address (str): Exchange contract address. Must be one of ['0x00000000000000adc04c56bf30ac9d3c0aaf14dc']
        quantity (Union[Unset, int]): The number of offers to place. Default: 1.
        offer_protection_enabled (Union[Unset, bool]): Builds the offer on OpenSea's signed zone to provide offer
            protections from receiving an item which is disabled from trading. Default: True.
    """

    offerer: str
    criteria: "Criteria"
    protocol_address: str
    quantity: Union[Unset, int] = 1
    offer_protection_enabled: Union[Unset, bool] = True

    def to_dict(self) -> Dict[str, Any]:
        offerer = self.offerer

        criteria = self.criteria.to_dict()

        protocol_address = self.protocol_address

        quantity = self.quantity

        offer_protection_enabled = self.offer_protection_enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "offerer": offerer,
                "criteria": criteria,
                "protocol_address": protocol_address,
            }
        )
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if offer_protection_enabled is not UNSET:
            field_dict["offer_protection_enabled"] = offer_protection_enabled

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        offerer = (None, str(self.offerer).encode(), "text/plain")

        criteria = (None, json.dumps(self.criteria.to_dict()).encode(), "application/json")

        protocol_address = (None, str(self.protocol_address).encode(), "text/plain")

        quantity = (
            self.quantity if isinstance(self.quantity, Unset) else (None, str(self.quantity).encode(), "text/plain")
        )

        offer_protection_enabled = (
            self.offer_protection_enabled
            if isinstance(self.offer_protection_enabled, Unset)
            else (None, str(self.offer_protection_enabled).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "offerer": offerer,
                "criteria": criteria,
                "protocol_address": protocol_address,
            }
        )
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if offer_protection_enabled is not UNSET:
            field_dict["offer_protection_enabled"] = offer_protection_enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.criteria import Criteria

        d = src_dict.copy()
        offerer = d.pop("offerer")

        criteria = Criteria.from_dict(d.pop("criteria"))

        protocol_address = d.pop("protocol_address")

        quantity = d.pop("quantity", UNSET)

        offer_protection_enabled = d.pop("offer_protection_enabled", UNSET)

        build_offer_input = cls(
            offerer=offerer,
            criteria=criteria,
            protocol_address=protocol_address,
            quantity=quantity,
            offer_protection_enabled=offer_protection_enabled,
        )

        return build_offer_input
