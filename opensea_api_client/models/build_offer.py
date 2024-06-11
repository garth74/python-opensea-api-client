from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.partial_parameters import PartialParameters


T = TypeVar("T", bound="BuildOffer")


@_attrs_define
class BuildOffer:
    """
    Attributes:
        partial_parameters (PartialParameters):
        encoded_token_ids (Union[Unset, str]): Represents a list of token ids which can be used to fulfill the criteria
            offer. When decoded using the provided SDK function, developers can now see a list of all tokens that could be
            used to fulfill the offer.
    """

    partial_parameters: "PartialParameters"
    encoded_token_ids: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        partial_parameters = self.partial_parameters.to_dict()

        encoded_token_ids = self.encoded_token_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "partialParameters": partial_parameters,
            }
        )
        if encoded_token_ids is not UNSET:
            field_dict["encoded_token_ids"] = encoded_token_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.partial_parameters import PartialParameters

        d = src_dict.copy()
        partial_parameters = PartialParameters.from_dict(d.pop("partialParameters"))

        encoded_token_ids = d.pop("encoded_token_ids", UNSET)

        build_offer = cls(
            partial_parameters=partial_parameters,
            encoded_token_ids=encoded_token_ids,
        )

        build_offer.additional_properties = d
        return build_offer

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
