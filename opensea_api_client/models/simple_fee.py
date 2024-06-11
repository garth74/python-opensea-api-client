from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.simple_account import SimpleAccount


T = TypeVar("T", bound="SimpleFee")


@_attrs_define
class SimpleFee:
    """
    Attributes:
        account (SimpleAccount):
        basis_points (str):
    """

    account: "SimpleAccount"
    basis_points: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account = self.account.to_dict()

        basis_points = self.basis_points

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account": account,
                "basis_points": basis_points,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.simple_account import SimpleAccount

        d = src_dict.copy()
        account = SimpleAccount.from_dict(d.pop("account"))

        basis_points = d.pop("basis_points")

        simple_fee = cls(
            account=account,
            basis_points=basis_points,
        )

        simple_fee.additional_properties = d
        return simple_fee

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
