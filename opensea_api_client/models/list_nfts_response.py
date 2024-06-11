from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.nft_model import NftModel


T = TypeVar("T", bound="ListNftsResponse")


@_attrs_define
class ListNftsResponse:
    """
    Attributes:
        nfts (List['NftModel']):
        next_ (str): Cursor for the next page of results
    """

    nfts: List["NftModel"]
    next_: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        nfts = []
        for nfts_item_data in self.nfts:
            nfts_item = nfts_item_data.to_dict()
            nfts.append(nfts_item)

        next_ = self.next_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nfts": nfts,
                "next": next_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.nft_model import NftModel

        d = src_dict.copy()
        nfts = []
        _nfts = d.pop("nfts")
        for nfts_item_data in _nfts:
            nfts_item = NftModel.from_dict(nfts_item_data)

            nfts.append(nfts_item)

        next_ = d.pop("next")

        list_nfts_response = cls(
            nfts=nfts,
            next_=next_,
        )

        list_nfts_response.additional_properties = d
        return list_nfts_response

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
