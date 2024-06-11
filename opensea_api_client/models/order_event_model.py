from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.chain_identifier import ChainIdentifier
from ..models.order_event_model_event_type_enum import OrderEventModelEventTypeEnum
from ..models.order_type import OrderType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.criteria import Criteria
    from ..models.event_payment_model import EventPaymentModel
    from ..models.nft_model import NftModel
    from ..models.order_event_model_asset_type_1 import OrderEventModelAssetType1
    from ..models.order_event_model_criteria_type_1 import OrderEventModelCriteriaType1


T = TypeVar("T", bound="OrderEventModel")


@_attrs_define
class OrderEventModel:
    """
    Attributes:
        order_hash (str): Order hash for the newly created order
        order_type (OrderType): An enumeration.
        chain (ChainIdentifier): OpenSea supported chains.
        protocol_address (str): Exchange contract address for the order
        start_date (int): The Posix timestamp at which the order was created
        expiration_date (int): The Posix timestamp at which the order will close. When no expiration date is set, this
            value will be 0.
        asset (Union['NftModel', 'OrderEventModelAssetType1']): The asset being listed or bid on. Empty object for
            collection or trait offers.
        quantity (int): Number of assets in the order
        maker (str): Maker of the order
        taker (str): Taker of the order. This will only be set for private listings.
        payment (EventPaymentModel):
        criteria (Union['Criteria', 'OrderEventModelCriteriaType1']): For collection and trait offers, this object will
            contain the criteria needed to fulfill the offer.
        event_type (Union[Unset, OrderEventModelEventTypeEnum]):  Default: OrderEventModelEventTypeEnum.ORDER.
    """

    order_hash: str
    order_type: OrderType
    chain: ChainIdentifier
    protocol_address: str
    start_date: int
    expiration_date: int
    asset: Union["NftModel", "OrderEventModelAssetType1"]
    quantity: int
    maker: str
    taker: str
    payment: "EventPaymentModel"
    criteria: Union["Criteria", "OrderEventModelCriteriaType1"]
    event_type: Union[Unset, OrderEventModelEventTypeEnum] = OrderEventModelEventTypeEnum.ORDER
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.criteria import Criteria
        from ..models.nft_model import NftModel

        order_hash = self.order_hash

        order_type = self.order_type.value

        chain = self.chain.value

        protocol_address = self.protocol_address

        start_date = self.start_date

        expiration_date = self.expiration_date

        asset: Dict[str, Any]
        if isinstance(self.asset, NftModel):
            asset = self.asset.to_dict()
        else:
            asset = self.asset.to_dict()

        quantity = self.quantity

        maker = self.maker

        taker = self.taker

        payment = self.payment.to_dict()

        criteria: Dict[str, Any]
        if isinstance(self.criteria, Criteria):
            criteria = self.criteria.to_dict()
        else:
            criteria = self.criteria.to_dict()

        event_type: Union[Unset, str] = UNSET
        if not isinstance(self.event_type, Unset):
            event_type = self.event_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "order_hash": order_hash,
                "order_type": order_type,
                "chain": chain,
                "protocol_address": protocol_address,
                "start_date": start_date,
                "expiration_date": expiration_date,
                "asset": asset,
                "quantity": quantity,
                "maker": maker,
                "taker": taker,
                "payment": payment,
                "criteria": criteria,
            }
        )
        if event_type is not UNSET:
            field_dict["event_type"] = event_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.criteria import Criteria
        from ..models.event_payment_model import EventPaymentModel
        from ..models.nft_model import NftModel
        from ..models.order_event_model_asset_type_1 import OrderEventModelAssetType1
        from ..models.order_event_model_criteria_type_1 import OrderEventModelCriteriaType1

        d = src_dict.copy()
        order_hash = d.pop("order_hash")

        order_type = OrderType(d.pop("order_type"))

        chain = ChainIdentifier(d.pop("chain"))

        protocol_address = d.pop("protocol_address")

        start_date = d.pop("start_date")

        expiration_date = d.pop("expiration_date")

        def _parse_asset(data: object) -> Union["NftModel", "OrderEventModelAssetType1"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                asset_type_0 = NftModel.from_dict(data)

                return asset_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            asset_type_1 = OrderEventModelAssetType1.from_dict(data)

            return asset_type_1

        asset = _parse_asset(d.pop("asset"))

        quantity = d.pop("quantity")

        maker = d.pop("maker")

        taker = d.pop("taker")

        payment = EventPaymentModel.from_dict(d.pop("payment"))

        def _parse_criteria(data: object) -> Union["Criteria", "OrderEventModelCriteriaType1"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                criteria_type_0 = Criteria.from_dict(data)

                return criteria_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            criteria_type_1 = OrderEventModelCriteriaType1.from_dict(data)

            return criteria_type_1

        criteria = _parse_criteria(d.pop("criteria"))

        _event_type = d.pop("event_type", UNSET)
        event_type: Union[Unset, OrderEventModelEventTypeEnum]
        if isinstance(_event_type, Unset):
            event_type = UNSET
        else:
            event_type = OrderEventModelEventTypeEnum(_event_type)

        order_event_model = cls(
            order_hash=order_hash,
            order_type=order_type,
            chain=chain,
            protocol_address=protocol_address,
            start_date=start_date,
            expiration_date=expiration_date,
            asset=asset,
            quantity=quantity,
            maker=maker,
            taker=taker,
            payment=payment,
            criteria=criteria,
            event_type=event_type,
        )

        order_event_model.additional_properties = d
        return order_event_model

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
