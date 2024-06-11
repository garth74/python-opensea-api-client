from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.order_type import OrderType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.consideration_item import ConsiderationItem
    from ..models.offer_item import OfferItem


T = TypeVar("T", bound="OrderInputComponents")


@_attrs_define
class OrderInputComponents:
    """
    Attributes:
        offerer (str): The address which supplies all the items in the offer.
        offer (List['OfferItem']): Array of items that may be transferred from the offerer's account.
        consideration (List['ConsiderationItem']): Array of items which must be received by a recipient to fulfill the
            order. One of the consideration items must be the OpenSea marketplace fee.
        start_time (int): The block timestamp at which the order becomes active
        end_time (int): The block timestamp at which the order expires.
        order_type (OrderType): An enumeration.
        zone (str): Optional secondary account attached the order which can cancel orders. Additionally, when the
            `OrderType` is Restricted, the zone or the offerer are the only entities which can execute the order.
            For open orders, use the zero address.
            For restricted orders, use the signed zone address <SIGNED_ZONE_ADDRESS>
        zone_hash (str): A value that will be supplied to the zone when fulfilling restricted orders that the zone can
            utilize when making a determination on whether to authorize the order. Most often this value will be the zero
            hash 0x0000000000000000000000000000000000000000000000000000000000000000
        salt (str): an arbitrary source of entropy for the order
        conduit_key (str): Indicates what conduit, if any, should be utilized as a source for token approvals when
            performing transfers. By default (i.e. when conduitKey is set to the zero hash), the offerer will grant transfer
            approvals to Seaport directly.
            To utilize OpenSea's conduit, use 0x0000007b02230091a7ed01230072f7006a004d60a8d4e71d599b8104250f0000
        counter (str): Must match the current counter for the given offerer. If you are unsure of the current counter,
            it can be [read from the
            contract](https://etherscan.io/address/0x00000000000000adc04c56bf30ac9d3c0aaf14dc#readContract#F2) on etherscan.
        total_original_consideration_items (Union[Unset, int]): Size of the consideration array.
    """

    offerer: str
    offer: List["OfferItem"]
    consideration: List["ConsiderationItem"]
    start_time: int
    end_time: int
    order_type: OrderType
    zone: str
    zone_hash: str
    salt: str
    conduit_key: str
    counter: str
    total_original_consideration_items: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        offerer = self.offerer

        offer = []
        for offer_item_data in self.offer:
            offer_item = offer_item_data.to_dict()
            offer.append(offer_item)

        consideration = []
        for consideration_item_data in self.consideration:
            consideration_item = consideration_item_data.to_dict()
            consideration.append(consideration_item)

        start_time = self.start_time

        end_time = self.end_time

        order_type = self.order_type.value

        zone = self.zone

        zone_hash = self.zone_hash

        salt = self.salt

        conduit_key = self.conduit_key

        counter = self.counter

        total_original_consideration_items = self.total_original_consideration_items

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "offerer": offerer,
                "offer": offer,
                "consideration": consideration,
                "startTime": start_time,
                "endTime": end_time,
                "orderType": order_type,
                "zone": zone,
                "zoneHash": zone_hash,
                "salt": salt,
                "conduitKey": conduit_key,
                "counter": counter,
            }
        )
        if total_original_consideration_items is not UNSET:
            field_dict["totalOriginalConsiderationItems"] = total_original_consideration_items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.consideration_item import ConsiderationItem
        from ..models.offer_item import OfferItem

        d = src_dict.copy()
        offerer = d.pop("offerer")

        offer = []
        _offer = d.pop("offer")
        for offer_item_data in _offer:
            offer_item = OfferItem.from_dict(offer_item_data)

            offer.append(offer_item)

        consideration = []
        _consideration = d.pop("consideration")
        for consideration_item_data in _consideration:
            consideration_item = ConsiderationItem.from_dict(consideration_item_data)

            consideration.append(consideration_item)

        start_time = d.pop("startTime")

        end_time = d.pop("endTime")

        order_type = OrderType(d.pop("orderType"))

        zone = d.pop("zone")

        zone_hash = d.pop("zoneHash")

        salt = d.pop("salt")

        conduit_key = d.pop("conduitKey")

        counter = d.pop("counter")

        total_original_consideration_items = d.pop("totalOriginalConsiderationItems", UNSET)

        order_input_components = cls(
            offerer=offerer,
            offer=offer,
            consideration=consideration,
            start_time=start_time,
            end_time=end_time,
            order_type=order_type,
            zone=zone,
            zone_hash=zone_hash,
            salt=salt,
            conduit_key=conduit_key,
            counter=counter,
            total_original_consideration_items=total_original_consideration_items,
        )

        order_input_components.additional_properties = d
        return order_input_components

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
