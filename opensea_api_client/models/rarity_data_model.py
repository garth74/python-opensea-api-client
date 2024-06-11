from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rarity_strategy_id import RarityStrategyId
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ranking_features import RankingFeatures


T = TypeVar("T", bound="RarityDataModel")


@_attrs_define
class RarityDataModel:
    """
    Attributes:
        rank (int): Rarity Rank of the NFT in the collection
        strategy_id (Union[Unset, RarityStrategyId]): Rarity algorithm used. Currently, always 'openrarity'
        strategy_version (Union[Unset, str]): Deprecated Field
        score (Union[Unset, float]): Deprecated Field
        calculated_at (Union[Unset, str]): Deprecated Field Default: ''.
        max_rank (Union[Unset, int]): Deprecated Field
        total_supply (Union[Unset, int]): Deprecated Field Default: 0.
        ranking_features (Union[Unset, RankingFeatures]):
    """

    rank: int
    strategy_id: Union[Unset, RarityStrategyId] = UNSET
    strategy_version: Union[Unset, str] = UNSET
    score: Union[Unset, float] = UNSET
    calculated_at: Union[Unset, str] = ""
    max_rank: Union[Unset, int] = UNSET
    total_supply: Union[Unset, int] = 0
    ranking_features: Union[Unset, "RankingFeatures"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rank = self.rank

        strategy_id: Union[Unset, str] = UNSET
        if not isinstance(self.strategy_id, Unset):
            strategy_id = self.strategy_id.value

        strategy_version = self.strategy_version

        score = self.score

        calculated_at = self.calculated_at

        max_rank = self.max_rank

        total_supply = self.total_supply

        ranking_features: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ranking_features, Unset):
            ranking_features = self.ranking_features.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rank": rank,
            }
        )
        if strategy_id is not UNSET:
            field_dict["strategy_id"] = strategy_id
        if strategy_version is not UNSET:
            field_dict["strategy_version"] = strategy_version
        if score is not UNSET:
            field_dict["score"] = score
        if calculated_at is not UNSET:
            field_dict["calculated_at"] = calculated_at
        if max_rank is not UNSET:
            field_dict["max_rank"] = max_rank
        if total_supply is not UNSET:
            field_dict["total_supply"] = total_supply
        if ranking_features is not UNSET:
            field_dict["ranking_features"] = ranking_features

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ranking_features import RankingFeatures

        d = src_dict.copy()
        rank = d.pop("rank")

        _strategy_id = d.pop("strategy_id", UNSET)
        strategy_id: Union[Unset, RarityStrategyId]
        if isinstance(_strategy_id, Unset):
            strategy_id = UNSET
        else:
            strategy_id = RarityStrategyId(_strategy_id)

        strategy_version = d.pop("strategy_version", UNSET)

        score = d.pop("score", UNSET)

        calculated_at = d.pop("calculated_at", UNSET)

        max_rank = d.pop("max_rank", UNSET)

        total_supply = d.pop("total_supply", UNSET)

        _ranking_features = d.pop("ranking_features", UNSET)
        ranking_features: Union[Unset, RankingFeatures]
        if isinstance(_ranking_features, Unset):
            ranking_features = UNSET
        else:
            ranking_features = RankingFeatures.from_dict(_ranking_features)

        rarity_data_model = cls(
            rank=rank,
            strategy_id=strategy_id,
            strategy_version=strategy_version,
            score=score,
            calculated_at=calculated_at,
            max_rank=max_rank,
            total_supply=total_supply,
            ranking_features=ranking_features,
        )

        rarity_data_model.additional_properties = d
        return rarity_data_model

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
