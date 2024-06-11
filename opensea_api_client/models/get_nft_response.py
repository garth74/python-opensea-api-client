from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.detailed_nft_model import DetailedNftModel


T = TypeVar("T", bound="GetNftResponse")


@_attrs_define
class GetNftResponse:
    """
    Attributes:
        nft (DetailedNftModel):
    """

    nft: "DetailedNftModel"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        nft = self.nft.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nft": nft,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.detailed_nft_model import DetailedNftModel

        d = src_dict.copy()
        nft = DetailedNftModel.from_dict(d.pop("nft"))

        get_nft_response = cls(
            nft=nft,
        )

        get_nft_response.additional_properties = d
        return get_nft_response

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
