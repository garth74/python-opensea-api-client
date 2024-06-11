import json
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.fulfiller_input import FulfillerInput
    from ..models.fulfillment_input import FulfillmentInput


T = TypeVar("T", bound="GenerateListingFulfillmentInput")


@_attrs_define
class GenerateListingFulfillmentInput:
    """
    Attributes:
        listing (FulfillmentInput):
        fulfiller (FulfillerInput):
    """

    listing: "FulfillmentInput"
    fulfiller: "FulfillerInput"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        listing = self.listing.to_dict()

        fulfiller = self.fulfiller.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "listing": listing,
                "fulfiller": fulfiller,
            }
        )

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        listing = (None, json.dumps(self.listing.to_dict()).encode(), "application/json")

        fulfiller = (None, json.dumps(self.fulfiller.to_dict()).encode(), "application/json")

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "listing": listing,
                "fulfiller": fulfiller,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fulfiller_input import FulfillerInput
        from ..models.fulfillment_input import FulfillmentInput

        d = src_dict.copy()
        listing = FulfillmentInput.from_dict(d.pop("listing"))

        fulfiller = FulfillerInput.from_dict(d.pop("fulfiller"))

        generate_listing_fulfillment_input = cls(
            listing=listing,
            fulfiller=fulfiller,
        )

        generate_listing_fulfillment_input.additional_properties = d
        return generate_listing_fulfillment_input

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
