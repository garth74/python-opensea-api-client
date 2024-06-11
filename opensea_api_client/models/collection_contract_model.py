from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.chain_identifier import ChainIdentifier

T = TypeVar("T", bound="CollectionContractModel")


@_attrs_define
class CollectionContractModel:
    """Define the Contract's Addresses and Chain

    Attributes:
        address (str): The unique public blockchain identifier, address, for the contract.
        chain (ChainIdentifier): OpenSea supported chains.
    """

    address: str
    chain: ChainIdentifier
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        address = self.address

        chain = self.chain.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "address": address,
                "chain": chain,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        address = d.pop("address")

        chain = ChainIdentifier(d.pop("chain"))

        collection_contract_model = cls(
            address=address,
            chain=chain,
        )

        collection_contract_model.additional_properties = d
        return collection_contract_model

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
