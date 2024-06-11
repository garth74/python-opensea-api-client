from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.order_input_with_protocol import OrderInputWithProtocol
from ...models.post_listing_chain import PostListingChain
from ...models.post_listing_protocol import PostListingProtocol
from ...types import Response


def _get_kwargs(
    chain: PostListingChain,
    protocol: PostListingProtocol,
    *,
    body: Union[
        OrderInputWithProtocol,
        OrderInputWithProtocol,
        OrderInputWithProtocol,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/api/v2/orders/{chain}/{protocol}/listings",
    }

    if isinstance(body, OrderInputWithProtocol):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, OrderInputWithProtocol):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, OrderInputWithProtocol):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
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
    chain: PostListingChain,
    protocol: PostListingProtocol,
    *,
    client: AuthenticatedClient,
    body: Union[
        OrderInputWithProtocol,
        OrderInputWithProtocol,
        OrderInputWithProtocol,
    ],
) -> Response[Any]:
    """Create Listing

     List a single NFT (ERC721 or ERC1155) for sale on the OpenSea marketplace.

    Args:
        chain (PostListingChain):
        protocol (PostListingProtocol):
        body (OrderInputWithProtocol):
        body (OrderInputWithProtocol):
        body (OrderInputWithProtocol):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        chain=chain,
        protocol=protocol,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    chain: PostListingChain,
    protocol: PostListingProtocol,
    *,
    client: AuthenticatedClient,
    body: Union[
        OrderInputWithProtocol,
        OrderInputWithProtocol,
        OrderInputWithProtocol,
    ],
) -> Response[Any]:
    """Create Listing

     List a single NFT (ERC721 or ERC1155) for sale on the OpenSea marketplace.

    Args:
        chain (PostListingChain):
        protocol (PostListingProtocol):
        body (OrderInputWithProtocol):
        body (OrderInputWithProtocol):
        body (OrderInputWithProtocol):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        chain=chain,
        protocol=protocol,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
