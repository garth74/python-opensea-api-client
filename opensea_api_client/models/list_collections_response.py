from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.collection_model import CollectionModel


T = TypeVar("T", bound="ListCollectionsResponse")


@_attrs_define
class ListCollectionsResponse:
    """
    Attributes:
        collections (List['CollectionModel']):
        next_ (str): Cursor for the next page of results
    """

    collections: List["CollectionModel"]
    next_: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        collections = []
        for collections_item_data in self.collections:
            collections_item = collections_item_data.to_dict()
            collections.append(collections_item)

        next_ = self.next_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collections": collections,
                "next": next_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.collection_model import CollectionModel

        d = src_dict.copy()
        collections = []
        _collections = d.pop("collections")
        for collections_item_data in _collections:
            collections_item = CollectionModel.from_dict(collections_item_data)

            collections.append(collections_item)

        next_ = d.pop("next")

        list_collections_response = cls(
            collections=collections,
            next_=next_,
        )

        list_collections_response.additional_properties = d
        return list_collections_response

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
