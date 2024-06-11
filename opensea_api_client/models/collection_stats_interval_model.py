from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.collection_stats_interval import CollectionStatsInterval

T = TypeVar("T", bound="CollectionStatsIntervalModel")


@_attrs_define
class CollectionStatsIntervalModel:
    """
    Attributes:
        interval (CollectionStatsInterval): The interval for which the stats are calculated
        volume (float): The volume of sales for the collection during the specified interval
        volume_diff (float): The volume differential compared to the previous interval
        volume_change (float): The percentage change in volume compared to the previous interval
        sales (int): The number of sales for the collection during the specified interval
        sales_diff (float): The percentage change in number of sales compared to the previous interval
        average_price (float): The average sale price of NFTs in the collection during the interval
    """

    interval: CollectionStatsInterval
    volume: float
    volume_diff: float
    volume_change: float
    sales: int
    sales_diff: float
    average_price: float
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        interval = self.interval.value

        volume = self.volume

        volume_diff = self.volume_diff

        volume_change = self.volume_change

        sales = self.sales

        sales_diff = self.sales_diff

        average_price = self.average_price

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "interval": interval,
                "volume": volume,
                "volume_diff": volume_diff,
                "volume_change": volume_change,
                "sales": sales,
                "sales_diff": sales_diff,
                "average_price": average_price,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        interval = CollectionStatsInterval(d.pop("interval"))

        volume = d.pop("volume")

        volume_diff = d.pop("volume_diff")

        volume_change = d.pop("volume_change")

        sales = d.pop("sales")

        sales_diff = d.pop("sales_diff")

        average_price = d.pop("average_price")

        collection_stats_interval_model = cls(
            interval=interval,
            volume=volume,
            volume_diff=volume_diff,
            volume_change=volume_change,
            sales=sales,
            sales_diff=sales_diff,
            average_price=average_price,
        )

        collection_stats_interval_model.additional_properties = d
        return collection_stats_interval_model

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
