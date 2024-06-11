import json
from typing import TYPE_CHECKING, Any, Dict, Tuple, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.consideration_input import ConsiderationInput
    from ..models.fulfiller_input import FulfillerInput
    from ..models.fulfillment_input import FulfillmentInput


T = TypeVar("T", bound="GenerateOfferFulfillmentInput")


@_attrs_define
class GenerateOfferFulfillmentInput:
    """
    Attributes:
        offer (FulfillmentInput):
        fulfiller (FulfillerInput):
        consideration (Union[Unset, ConsiderationInput]):
    """

    offer: "FulfillmentInput"
    fulfiller: "FulfillerInput"
    consideration: Union[Unset, "ConsiderationInput"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        offer = self.offer.to_dict()

        fulfiller = self.fulfiller.to_dict()

        consideration: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.consideration, Unset):
            consideration = self.consideration.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "offer": offer,
                "fulfiller": fulfiller,
            }
        )
        if consideration is not UNSET:
            field_dict["consideration"] = consideration

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        offer = (None, json.dumps(self.offer.to_dict()).encode(), "application/json")

        fulfiller = (None, json.dumps(self.fulfiller.to_dict()).encode(), "application/json")

        consideration: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.consideration, Unset):
            consideration = (None, json.dumps(self.consideration.to_dict()).encode(), "application/json")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "offer": offer,
                "fulfiller": fulfiller,
            }
        )
        if consideration is not UNSET:
            field_dict["consideration"] = consideration

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.consideration_input import ConsiderationInput
        from ..models.fulfiller_input import FulfillerInput
        from ..models.fulfillment_input import FulfillmentInput

        d = src_dict.copy()
        offer = FulfillmentInput.from_dict(d.pop("offer"))

        fulfiller = FulfillerInput.from_dict(d.pop("fulfiller"))

        _consideration = d.pop("consideration", UNSET)
        consideration: Union[Unset, ConsiderationInput]
        if isinstance(_consideration, Unset):
            consideration = UNSET
        else:
            consideration = ConsiderationInput.from_dict(_consideration)

        generate_offer_fulfillment_input = cls(
            offer=offer,
            fulfiller=fulfiller,
            consideration=consideration,
        )

        return generate_offer_fulfillment_input
