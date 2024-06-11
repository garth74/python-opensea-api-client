from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    collection_slug: str,
    *,
    float_value: Union[Unset, float] = UNSET,
    int_value: Union[Unset, int] = UNSET,
    type: Union[Unset, str] = UNSET,
    value: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["float_value"] = float_value

    params["int_value"] = int_value

    params["type"] = type

    params["value"] = value

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2/offers/collection/{collection_slug}/traits",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.BAD_REQUEST:
        return None
    if response.status_code == HTTPStatus.NOT_FOUND:
        return None
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    collection_slug: str,
    *,
    client: AuthenticatedClient,
    float_value: Union[Unset, float] = UNSET,
    int_value: Union[Unset, int] = UNSET,
    type: Union[Unset, str] = UNSET,
    value: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Get Trait Offers

     Get the active, valid trait offers for the specified collection.

    Args:
        collection_slug (str):
        float_value (Union[Unset, float]):
        int_value (Union[Unset, int]):
        type (Union[Unset, str]):
        value (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        collection_slug=collection_slug,
        float_value=float_value,
        int_value=int_value,
        type=type,
        value=value,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    collection_slug: str,
    *,
    client: AuthenticatedClient,
    float_value: Union[Unset, float] = UNSET,
    int_value: Union[Unset, int] = UNSET,
    type: Union[Unset, str] = UNSET,
    value: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Get Trait Offers

     Get the active, valid trait offers for the specified collection.

    Args:
        collection_slug (str):
        float_value (Union[Unset, float]):
        int_value (Union[Unset, int]):
        type (Union[Unset, str]):
        value (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        collection_slug=collection_slug,
        float_value=float_value,
        int_value=int_value,
        type=type,
        value=value,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
