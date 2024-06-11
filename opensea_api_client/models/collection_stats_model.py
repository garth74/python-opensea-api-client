from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CollectionStatsModel")


@_attrs_define
class CollectionStatsModel:
    """
    Attributes:
        volume (float): The all time volume of sales for the collection
        sales (int): The all time number of sales for the collection
        average_price (float): The all time average sale price of NFTs in the collection
        num_owners (int): The current number of unique owners of NFTs in the collection
        market_cap (float): The current market cap of the collection
        floor_price (float): The current lowest price of NFTs in the collection
        floor_price_symbol (str): The symbol of the payment asset for the floor price
    """

    volume: float
    sales: int
    average_price: float
    num_owners: int
    market_cap: float
    floor_price: float
    floor_price_symbol: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        volume = self.volume

        sales = self.sales

        average_price = self.average_price

        num_owners = self.num_owners

        market_cap = self.market_cap

        floor_price = self.floor_price

        floor_price_symbol = self.floor_price_symbol

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "volume": volume,
                "sales": sales,
                "average_price": average_price,
                "num_owners": num_owners,
                "market_cap": market_cap,
                "floor_price": floor_price,
                "floor_price_symbol": floor_price_symbol,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        volume = d.pop("volume")

        sales = d.pop("sales")

        average_price = d.pop("average_price")

        num_owners = d.pop("num_owners")

        market_cap = d.pop("market_cap")

        floor_price = d.pop("floor_price")

        floor_price_symbol = d.pop("floor_price_symbol")

        collection_stats_model = cls(
            volume=volume,
            sales=sales,
            average_price=average_price,
            num_owners=num_owners,
            market_cap=market_cap,
            floor_price=floor_price,
            floor_price_symbol=floor_price_symbol,
        )

        collection_stats_model.additional_properties = d
        return collection_stats_model

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
