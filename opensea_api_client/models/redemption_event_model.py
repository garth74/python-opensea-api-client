from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.chain_identifier import ChainIdentifier
from ..models.redemption_event_model_event_type_enum import RedemptionEventModelEventTypeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nft_model import NftModel
    from ..models.redemption_event_model_asset_type_1 import RedemptionEventModelAssetType1


T = TypeVar("T", bound="RedemptionEventModel")


@_attrs_define
class RedemptionEventModel:
    """
    Attributes:
        chain (ChainIdentifier): OpenSea supported chains.
        from_address (str): Address of the sender
        to_address (str): Address of the recipient
        asset (Union['NftModel', 'RedemptionEventModelAssetType1']): The asset being redeemed.
        quantity (int): Number of assets redeemed
        transaction (str): Transaction hash for the redemption
        event_type (Union[Unset, RedemptionEventModelEventTypeEnum]):  Default:
            RedemptionEventModelEventTypeEnum.REDEMPTION.
    """

    chain: ChainIdentifier
    from_address: str
    to_address: str
    asset: Union["NftModel", "RedemptionEventModelAssetType1"]
    quantity: int
    transaction: str
    event_type: Union[Unset, RedemptionEventModelEventTypeEnum] = RedemptionEventModelEventTypeEnum.REDEMPTION
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.nft_model import NftModel

        chain = self.chain.value

        from_address = self.from_address

        to_address = self.to_address

        asset: Dict[str, Any]
        if isinstance(self.asset, NftModel):
            asset = self.asset.to_dict()
        else:
            asset = self.asset.to_dict()

        quantity = self.quantity

        transaction = self.transaction

        event_type: Union[Unset, str] = UNSET
        if not isinstance(self.event_type, Unset):
            event_type = self.event_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chain": chain,
                "from_address": from_address,
                "to_address": to_address,
                "asset": asset,
                "quantity": quantity,
                "transaction": transaction,
            }
        )
        if event_type is not UNSET:
            field_dict["event_type"] = event_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.nft_model import NftModel
        from ..models.redemption_event_model_asset_type_1 import RedemptionEventModelAssetType1

        d = src_dict.copy()
        chain = ChainIdentifier(d.pop("chain"))

        from_address = d.pop("from_address")

        to_address = d.pop("to_address")

        def _parse_asset(data: object) -> Union["NftModel", "RedemptionEventModelAssetType1"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                asset_type_0 = NftModel.from_dict(data)

                return asset_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            asset_type_1 = RedemptionEventModelAssetType1.from_dict(data)

            return asset_type_1

        asset = _parse_asset(d.pop("asset"))

        quantity = d.pop("quantity")

        transaction = d.pop("transaction")

        _event_type = d.pop("event_type", UNSET)
        event_type: Union[Unset, RedemptionEventModelEventTypeEnum]
        if isinstance(_event_type, Unset):
            event_type = UNSET
        else:
            event_type = RedemptionEventModelEventTypeEnum(_event_type)

        redemption_event_model = cls(
            chain=chain,
            from_address=from_address,
            to_address=to_address,
            asset=asset,
            quantity=quantity,
            transaction=transaction,
            event_type=event_type,
        )

        redemption_event_model.additional_properties = d
        return redemption_event_model

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
