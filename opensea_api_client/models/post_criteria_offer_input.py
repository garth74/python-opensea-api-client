import json
from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.criteria import Criteria
    from ..models.order_input import OrderInput


T = TypeVar("T", bound="PostCriteriaOfferInput")


@_attrs_define
class PostCriteriaOfferInput:
    """
    Attributes:
        protocol_data (OrderInput):
        criteria (Criteria):
        protocol_address (str): Exchange contract address. Must be one of ['0x00000000000000adc04c56bf30ac9d3c0aaf14dc']
    """

    protocol_data: "OrderInput"
    criteria: "Criteria"
    protocol_address: str

    def to_dict(self) -> Dict[str, Any]:
        protocol_data = self.protocol_data.to_dict()

        criteria = self.criteria.to_dict()

        protocol_address = self.protocol_address

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "protocol_data": protocol_data,
                "criteria": criteria,
                "protocol_address": protocol_address,
            }
        )

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        protocol_data = (None, json.dumps(self.protocol_data.to_dict()).encode(), "application/json")

        criteria = (None, json.dumps(self.criteria.to_dict()).encode(), "application/json")

        protocol_address = (None, str(self.protocol_address).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "protocol_data": protocol_data,
                "criteria": criteria,
                "protocol_address": protocol_address,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.criteria import Criteria
        from ..models.order_input import OrderInput

        d = src_dict.copy()
        protocol_data = OrderInput.from_dict(d.pop("protocol_data"))

        criteria = Criteria.from_dict(d.pop("criteria"))

        protocol_address = d.pop("protocol_address")

        post_criteria_offer_input = cls(
            protocol_data=protocol_data,
            criteria=criteria,
            protocol_address=protocol_address,
        )

        return post_criteria_offer_input
