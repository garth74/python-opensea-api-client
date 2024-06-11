from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_nfts_by_contract_chain import ListNftsByContractChain
from ...models.list_nfts_response import ListNftsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    chain: ListNftsByContractChain,
    address: str,
    *,
    limit: Union[Unset, int] = UNSET,
    next_: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["limit"] = limit

    params["next"] = next_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2/chain/{chain}/contract/{address}/nfts",
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
    chain: ListNftsByContractChain,
    address: str,
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, int] = UNSET,
    next_: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ListNftsResponse]]:
    """Get NFTs (by contract)

     Get multiple NFTs for a smart contract.

    Args:
        chain (ListNftsByContractChain):
        address (str):
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
        limit=limit,
        next_=next_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    chain: ListNftsByContractChain,
    address: str,
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, int] = UNSET,
    next_: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ListNftsResponse]]:
    """Get NFTs (by contract)

     Get multiple NFTs for a smart contract.

    Args:
        chain (ListNftsByContractChain):
        address (str):
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
        limit=limit,
        next_=next_,
    ).parsed


async def asyncio_detailed(
    chain: ListNftsByContractChain,
    address: str,
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, int] = UNSET,
    next_: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ListNftsResponse]]:
    """Get NFTs (by contract)

     Get multiple NFTs for a smart contract.

    Args:
        chain (ListNftsByContractChain):
        address (str):
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
        limit=limit,
        next_=next_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    chain: ListNftsByContractChain,
    address: str,
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, int] = UNSET,
    next_: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ListNftsResponse]]:
    """Get NFTs (by contract)

     Get multiple NFTs for a smart contract.

    Args:
        chain (ListNftsByContractChain):
        address (str):
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
            limit=limit,
            next_=next_,
        )
    ).parsed
