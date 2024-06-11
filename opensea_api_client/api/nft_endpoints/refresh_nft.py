from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.refresh_nft_chain import RefreshNftChain
from ...types import Response


def _get_kwargs(
    chain: RefreshNftChain,
    address: str,
    identifier: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/api/v2/chain/{chain}/contract/{address}/nfts/{identifier}/refresh",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.OK:
        return None
    if response.status_code == HTTPStatus.BAD_REQUEST:
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
    chain: RefreshNftChain,
    address: str,
    identifier: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """Refresh NFT Metadata

     Refresh metadata for a single NFT.

    Args:
        chain (RefreshNftChain):
        address (str):
        identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
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


async def asyncio_detailed(
    chain: RefreshNftChain,
    address: str,
    identifier: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """Refresh NFT Metadata

     Refresh metadata for a single NFT.

    Args:
        chain (RefreshNftChain):
        address (str):
        identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        chain=chain,
        address=address,
        identifier=identifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
