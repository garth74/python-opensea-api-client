from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.listing import Listing
    from ..models.offer import Offer


T = TypeVar("T", bound="GetOrderResult")


@_attrs_define
class GetOrderResult:
    """
    Attributes:
        order (Union['Listing', 'Offer']):
    """

    order: Union["Listing", "Offer"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.listing import Listing

        order: Dict[str, Any]
        if isinstance(self.order, Listing):
            order = self.order.to_dict()
        else:
            order = self.order.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "order": order,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.listing import Listing
        from ..models.offer import Offer

        d = src_dict.copy()

        def _parse_order(data: object) -> Union["Listing", "Offer"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                order_type_0 = Listing.from_dict(data)

                return order_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            order_type_1 = Offer.from_dict(data)

            return order_type_1

        order = _parse_order(d.pop("order"))

        get_order_result = cls(
            order=order,
        )

        get_order_result.additional_properties = d
        return get_order_result

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
