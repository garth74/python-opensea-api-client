import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_listings_chain import GetListingsChain
from ...models.get_listings_order_by import GetListingsOrderBy
from ...models.get_listings_order_direction import GetListingsOrderDirection
from ...models.get_listings_protocol import GetListingsProtocol
from ...types import UNSET, Response, Unset


def _get_kwargs(
    chain: GetListingsChain,
    protocol: GetListingsProtocol,
    *,
    asset_contract_address: Union[Unset, str] = UNSET,
    bundled: Union[Unset, bool] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    listed_after: Union[Unset, datetime.datetime] = UNSET,
    listed_before: Union[Unset, datetime.datetime] = UNSET,
    maker: Union[Unset, str] = UNSET,
    order_by: Union[Unset, GetListingsOrderBy] = UNSET,
    order_direction: Union[Unset, GetListingsOrderDirection] = UNSET,
    payment_token_address: Union[Unset, str] = UNSET,
    taker: Union[Unset, str] = UNSET,
    token_ids: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["asset_contract_address"] = asset_contract_address

    params["bundled"] = bundled

    params["cursor"] = cursor

    params["limit"] = limit

    json_listed_after: Union[Unset, str] = UNSET
    if not isinstance(listed_after, Unset):
        json_listed_after = listed_after.isoformat()
    params["listed_after"] = json_listed_after

    json_listed_before: Union[Unset, str] = UNSET
    if not isinstance(listed_before, Unset):
        json_listed_before = listed_before.isoformat()
    params["listed_before"] = json_listed_before

    params["maker"] = maker

    json_order_by: Union[Unset, str] = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by.value

    params["order_by"] = json_order_by

    json_order_direction: Union[Unset, str] = UNSET
    if not isinstance(order_direction, Unset):
        json_order_direction = order_direction.value

    params["order_direction"] = json_order_direction

    params["payment_token_address"] = payment_token_address

    params["taker"] = taker

    params["token_ids"] = token_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2/orders/{chain}/{protocol}/listings",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
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
    chain: GetListingsChain,
    protocol: GetListingsProtocol,
    *,
    client: AuthenticatedClient,
    asset_contract_address: Union[Unset, str] = UNSET,
    bundled: Union[Unset, bool] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    listed_after: Union[Unset, datetime.datetime] = UNSET,
    listed_before: Union[Unset, datetime.datetime] = UNSET,
    maker: Union[Unset, str] = UNSET,
    order_by: Union[Unset, GetListingsOrderBy] = UNSET,
    order_direction: Union[Unset, GetListingsOrderDirection] = UNSET,
    payment_token_address: Union[Unset, str] = UNSET,
    taker: Union[Unset, str] = UNSET,
    token_ids: Union[Unset, int] = UNSET,
) -> Response[Any]:
    """Get Listings

     Get the complete set of active, valid listings.

    Args:
        chain (GetListingsChain):
        protocol (GetListingsProtocol):
        asset_contract_address (Union[Unset, str]):
        bundled (Union[Unset, bool]):
        cursor (Union[Unset, str]):
        limit (Union[Unset, int]):
        listed_after (Union[Unset, datetime.datetime]):
        listed_before (Union[Unset, datetime.datetime]):
        maker (Union[Unset, str]):
        order_by (Union[Unset, GetListingsOrderBy]):
        order_direction (Union[Unset, GetListingsOrderDirection]):
        payment_token_address (Union[Unset, str]):
        taker (Union[Unset, str]):
        token_ids (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        chain=chain,
        protocol=protocol,
        asset_contract_address=asset_contract_address,
        bundled=bundled,
        cursor=cursor,
        limit=limit,
        listed_after=listed_after,
        listed_before=listed_before,
        maker=maker,
        order_by=order_by,
        order_direction=order_direction,
        payment_token_address=payment_token_address,
        taker=taker,
        token_ids=token_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    chain: GetListingsChain,
    protocol: GetListingsProtocol,
    *,
    client: AuthenticatedClient,
    asset_contract_address: Union[Unset, str] = UNSET,
    bundled: Union[Unset, bool] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    listed_after: Union[Unset, datetime.datetime] = UNSET,
    listed_before: Union[Unset, datetime.datetime] = UNSET,
    maker: Union[Unset, str] = UNSET,
    order_by: Union[Unset, GetListingsOrderBy] = UNSET,
    order_direction: Union[Unset, GetListingsOrderDirection] = UNSET,
    payment_token_address: Union[Unset, str] = UNSET,
    taker: Union[Unset, str] = UNSET,
    token_ids: Union[Unset, int] = UNSET,
) -> Response[Any]:
    """Get Listings

     Get the complete set of active, valid listings.

    Args:
        chain (GetListingsChain):
        protocol (GetListingsProtocol):
        asset_contract_address (Union[Unset, str]):
        bundled (Union[Unset, bool]):
        cursor (Union[Unset, str]):
        limit (Union[Unset, int]):
        listed_after (Union[Unset, datetime.datetime]):
        listed_before (Union[Unset, datetime.datetime]):
        maker (Union[Unset, str]):
        order_by (Union[Unset, GetListingsOrderBy]):
        order_direction (Union[Unset, GetListingsOrderDirection]):
        payment_token_address (Union[Unset, str]):
        taker (Union[Unset, str]):
        token_ids (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        chain=chain,
        protocol=protocol,
        asset_contract_address=asset_contract_address,
        bundled=bundled,
        cursor=cursor,
        limit=limit,
        listed_after=listed_after,
        listed_before=listed_before,
        maker=maker,
        order_by=order_by,
        order_direction=order_direction,
        payment_token_address=payment_token_address,
        taker=taker,
        token_ids=token_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
