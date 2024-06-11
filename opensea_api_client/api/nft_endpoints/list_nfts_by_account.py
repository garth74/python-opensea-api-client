from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_nfts_by_account_chain import ListNftsByAccountChain
from ...models.list_nfts_response import ListNftsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    chain: ListNftsByAccountChain,
    address: str,
    *,
    collection: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    next_: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["collection"] = collection

    params["limit"] = limit

    params["next"] = next_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2/chain/{chain}/account/{address}/nfts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ListNftsResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ListNftsResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ListNftsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    chain: ListNftsByAccountChain,
    address: str,
    *,
    client: AuthenticatedClient,
    collection: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    next_: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ListNftsResponse]]:
    """Get NFTs (by account)

     Get NFTs owned by a given account address.

    Args:
        chain (ListNftsByAccountChain):
        address (str):
        collection (Union[Unset, str]):
        limit (Union[Unset, int]):
        next_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ListNftsResponse]]
    """

    kwargs = _get_kwargs(
        chain=chain,
        address=address,
        collection=collection,
        limit=limit,
        next_=next_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    chain: ListNftsByAccountChain,
    address: str,
    *,
    client: AuthenticatedClient,
    collection: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    next_: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ListNftsResponse]]:
    """Get NFTs (by account)

     Get NFTs owned by a given account address.

    Args:
        chain (ListNftsByAccountChain):
        address (str):
        collection (Union[Unset, str]):
        limit (Union[Unset, int]):
        next_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ListNftsResponse]
    """

    return sync_detailed(
        chain=chain,
        address=address,
        client=client,
        collection=collection,
        limit=limit,
        next_=next_,
    ).parsed


async def asyncio_detailed(
    chain: ListNftsByAccountChain,
    address: str,
    *,
    client: AuthenticatedClient,
    collection: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    next_: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ListNftsResponse]]:
    """Get NFTs (by account)

     Get NFTs owned by a given account address.

    Args:
        chain (ListNftsByAccountChain):
        address (str):
        collection (Union[Unset, str]):
        limit (Union[Unset, int]):
        next_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ListNftsResponse]]
    """

    kwargs = _get_kwargs(
        chain=chain,
        address=address,
        collection=collection,
        limit=limit,
        next_=next_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    chain: ListNftsByAccountChain,
    address: str,
    *,
    client: AuthenticatedClient,
    collection: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    next_: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ListNftsResponse]]:
    """Get NFTs (by account)

     Get NFTs owned by a given account address.

    Args:
        chain (ListNftsByAccountChain):
        address (str):
        collection (Union[Unset, str]):
        limit (Union[Unset, int]):
        next_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ListNftsResponse]
    """

    return (
        await asyncio_detailed(
            chain=chain,
            address=address,
            client=client,
            collection=collection,
            limit=limit,
            next_=next_,
        )
    ).parsed
