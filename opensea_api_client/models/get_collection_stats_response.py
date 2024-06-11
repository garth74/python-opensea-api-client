from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.collection_stats_interval_model import CollectionStatsIntervalModel
    from ..models.collection_stats_model import CollectionStatsModel


T = TypeVar("T", bound="GetCollectionStatsResponse")


@_attrs_define
class GetCollectionStatsResponse:
    """
    Attributes:
        total (CollectionStatsModel):
        intervals (List['CollectionStatsIntervalModel']): The stats for each interval
    """

    total: "CollectionStatsModel"
    intervals: List["CollectionStatsIntervalModel"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total = self.total.to_dict()

        intervals = []
        for intervals_item_data in self.intervals:
            intervals_item = intervals_item_data.to_dict()
            intervals.append(intervals_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "intervals": intervals,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.collection_stats_interval_model import CollectionStatsIntervalModel
        from ..models.collection_stats_model import CollectionStatsModel

        d = src_dict.copy()
        total = CollectionStatsModel.from_dict(d.pop("total"))

        intervals = []
        _intervals = d.pop("intervals")
        for intervals_item_data in _intervals:
            intervals_item = CollectionStatsIntervalModel.from_dict(intervals_item_data)

            intervals.append(intervals_item)

        get_collection_stats_response = cls(
            total=total,
            intervals=intervals,
        )

        get_collection_stats_response.additional_properties = d
        return get_collection_stats_response

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
