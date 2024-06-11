from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.cancel_event_model import CancelEventModel
    from ..models.order_event_model import OrderEventModel
    from ..models.redemption_event_model import RedemptionEventModel
    from ..models.sale_event_model import SaleEventModel
    from ..models.transfer_event_model import TransferEventModel


T = TypeVar("T", bound="ListEventsResponse")


@_attrs_define
class ListEventsResponse:
    """
    Attributes:
        asset_events (List[Union['CancelEventModel', 'OrderEventModel', 'RedemptionEventModel', 'SaleEventModel',
            'TransferEventModel']]):
        next_ (str): Cursor for the next page of results
    """

    asset_events: List[
        Union["CancelEventModel", "OrderEventModel", "RedemptionEventModel", "SaleEventModel", "TransferEventModel"]
    ]
    next_: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.cancel_event_model import CancelEventModel
        from ..models.order_event_model import OrderEventModel
        from ..models.sale_event_model import SaleEventModel
        from ..models.transfer_event_model import TransferEventModel

        asset_events = []
        for asset_events_item_data in self.asset_events:
            asset_events_item: Dict[str, Any]
            if isinstance(asset_events_item_data, CancelEventModel):
                asset_events_item = asset_events_item_data.to_dict()
            elif isinstance(asset_events_item_data, OrderEventModel):
                asset_events_item = asset_events_item_data.to_dict()
            elif isinstance(asset_events_item_data, SaleEventModel):
                asset_events_item = asset_events_item_data.to_dict()
            elif isinstance(asset_events_item_data, TransferEventModel):
                asset_events_item = asset_events_item_data.to_dict()
            else:
                asset_events_item = asset_events_item_data.to_dict()

            asset_events.append(asset_events_item)

        next_ = self.next_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "asset_events": asset_events,
                "next": next_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.cancel_event_model import CancelEventModel
        from ..models.order_event_model import OrderEventModel
        from ..models.redemption_event_model import RedemptionEventModel
        from ..models.sale_event_model import SaleEventModel
        from ..models.transfer_event_model import TransferEventModel

        d = src_dict.copy()
        asset_events = []
        _asset_events = d.pop("asset_events")
        for asset_events_item_data in _asset_events:

            def _parse_asset_events_item(
                data: object,
            ) -> Union[
                "CancelEventModel", "OrderEventModel", "RedemptionEventModel", "SaleEventModel", "TransferEventModel"
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    asset_events_item_type_0 = CancelEventModel.from_dict(data)

                    return asset_events_item_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    asset_events_item_type_1 = OrderEventModel.from_dict(data)

                    return asset_events_item_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    asset_events_item_type_2 = SaleEventModel.from_dict(data)

                    return asset_events_item_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    asset_events_item_type_3 = TransferEventModel.from_dict(data)

                    return asset_events_item_type_3
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                asset_events_item_type_4 = RedemptionEventModel.from_dict(data)

                return asset_events_item_type_4

            asset_events_item = _parse_asset_events_item(asset_events_item_data)

            asset_events.append(asset_events_item)

        next_ = d.pop("next")

        list_events_response = cls(
            asset_events=asset_events,
            next_=next_,
        )

        list_events_response.additional_properties = d
        return list_events_response

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
