import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.display_type_field import DisplayTypeField
from ..types import UNSET, Unset

T = TypeVar("T", bound="TraitModel")


@_attrs_define
class TraitModel:
    """
    Attributes:
        trait_type (str): The name of the trait category (e.g. 'Background')
        max_value (str): Ceiling for possible numeric trait values
        value (Union[datetime.date, float, int, str]): The value of the trait (e.g. 'Red')
        display_type (Union[Unset, DisplayTypeField]): A field indicating how to display. None is used for string
            traits.
        trait_count (Union[Unset, int]): Deprecated Field. Use Get Collection API instead.
        order (Union[Unset, int]): Deprecated Field
    """

    trait_type: str
    max_value: str
    value: Union[datetime.date, float, int, str]
    display_type: Union[Unset, DisplayTypeField] = UNSET
    trait_count: Union[Unset, int] = UNSET
    order: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        trait_type = self.trait_type

        max_value = self.max_value

        value: Union[float, int, str]
        if isinstance(self.value, datetime.date):
            value = self.value.isoformat()
        else:
            value = self.value

        display_type: Union[Unset, str] = UNSET
        if not isinstance(self.display_type, Unset):
            display_type = self.display_type.value

        trait_count = self.trait_count

        order = self.order

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "trait_type": trait_type,
                "max_value": max_value,
                "value": value,
            }
        )
        if display_type is not UNSET:
            field_dict["display_type"] = display_type
        if trait_count is not UNSET:
            field_dict["trait_count"] = trait_count
        if order is not UNSET:
            field_dict["order"] = order

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        trait_type = d.pop("trait_type")

        max_value = d.pop("max_value")

        def _parse_value(data: object) -> Union[datetime.date, float, int, str]:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                value_type_2 = isoparse(data).date()

                return value_type_2
            except:  # noqa: E722
                pass
            return cast(Union[datetime.date, float, int, str], data)

        value = _parse_value(d.pop("value"))

        _display_type = d.pop("display_type", UNSET)
        display_type: Union[Unset, DisplayTypeField]
        if isinstance(_display_type, Unset):
            display_type = UNSET
        else:
            display_type = DisplayTypeField(_display_type)

        trait_count = d.pop("trait_count", UNSET)

        order = d.pop("order", UNSET)

        trait_model = cls(
            trait_type=trait_type,
            max_value=max_value,
            value=value,
            display_type=display_type,
            trait_count=trait_count,
            order=order,
        )

        trait_model.additional_properties = d
        return trait_model

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
