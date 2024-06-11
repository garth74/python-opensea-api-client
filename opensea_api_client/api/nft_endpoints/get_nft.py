from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_nft_chain import GetNftChain
from ...models.get_nft_response import GetNftResponse
from ...types import Response


def _get_kwargs(
    chain: GetNftChain,
    address: str,
    identifier: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2/chain/{chain}/contract/{address}/nfts/{identifier}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetNftResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetNftResponse.from_dict(response.json())

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
) -> Response[Union[Any, GetNftResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    chain: GetNftChain,
    address: str,
    identifier: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, GetNftResponse]]:
    """Get an NFT

     Get metadata, traits, ownership information, and rarity for a single NFT.

    Args:
        chain (GetNftChain):
        address (str):
        identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetNftResponse]]
    """

    kwargs = _get_kwargs(
        chain=chain,
        address=address,
        identifier=identifier,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    chain: GetNftChain,
    address: str,
    identifier: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, GetNftResponse]]:
    """Get an NFT

     Get metadata, traits, ownership information, and rarity for a single NFT.

    Args:
        chain (GetNftChain):
        address (str):
        identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetNftResponse]
    """

    return sync_detailed(
        chain=chain,
        address=address,
        identifier=identifier,
        client=client,
    ).parsed


async def asyncio_detailed(
    chain: GetNftChain,
    address: str,
    identifier: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, GetNftResponse]]:
    """Get an NFT

     Get metadata, traits, ownership information, and rarity for a single NFT.

    Args:
        chain (GetNftChain):
        address (str):
        identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetNftResponse]]
    """

    kwargs = _get_kwargs(
        chain=chain,
        address=address,
        identifier=identifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    chain: GetNftChain,
    address: str,
    identifier: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, GetNftResponse]]:
    """Get an NFT

     Get metadata, traits, ownership information, and rarity for a single NFT.

    Args:
        chain (GetNftChain):
        address (str):
        identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetNftResponse]
    """

    return (
        await asyncio_detailed(
            chain=chain,
            address=address,
            identifier=identifier,
            client=client,
        )
    ).parsed
