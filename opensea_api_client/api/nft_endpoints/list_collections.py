from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_collections_response import ListCollectionsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    chain_identifier: Union[Unset, str] = UNSET,
    include_hidden: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    next_: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["chain_identifier"] = chain_identifier

    params["include_hidden"] = include_hidden

    params["limit"] = limit

    params["next"] = next_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/collections",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ListCollectionsResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ListCollectionsResponse.from_dict(response.json())

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
) -> Response[Union[Any, ListCollectionsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    chain_identifier: Union[Unset, str] = UNSET,
    include_hidden: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    next_: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ListCollectionsResponse]]:
    """Get Collections

     Get a list of OpenSea collections.

    Args:
        chain_identifier (Union[Unset, str]):
        include_hidden (Union[Unset, bool]):
        limit (Union[Unset, int]):
        next_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ListCollectionsResponse]]
    """

    kwargs = _get_kwargs(
        chain_identifier=chain_identifier,
        include_hidden=include_hidden,
        limit=limit,
        next_=next_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    chain_identifier: Union[Unset, str] = UNSET,
    include_hidden: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    next_: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ListCollectionsResponse]]:
    """Get Collections

     Get a list of OpenSea collections.

    Args:
        chain_identifier (Union[Unset, str]):
        include_hidden (Union[Unset, bool]):
        limit (Union[Unset, int]):
        next_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ListCollectionsResponse]
    """

    return sync_detailed(
        client=client,
        chain_identifier=chain_identifier,
        include_hidden=include_hidden,
        limit=limit,
        next_=next_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    chain_identifier: Union[Unset, str] = UNSET,
    include_hidden: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    next_: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ListCollectionsResponse]]:
    """Get Collections

     Get a list of OpenSea collections.

    Args:
        chain_identifier (Union[Unset, str]):
        include_hidden (Union[Unset, bool]):
        limit (Union[Unset, int]):
        next_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ListCollectionsResponse]]
    """

    kwargs = _get_kwargs(
        chain_identifier=chain_identifier,
        include_hidden=include_hidden,
        limit=limit,
        next_=next_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    chain_identifier: Union[Unset, str] = UNSET,
    include_hidden: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    next_: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ListCollectionsResponse]]:
    """Get Collections

     Get a list of OpenSea collections.

    Args:
        chain_identifier (Union[Unset, str]):
        include_hidden (Union[Unset, bool]):
        limit (Union[Unset, int]):
        next_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ListCollectionsResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            chain_identifier=chain_identifier,
            include_hidden=include_hidden,
            limit=limit,
            next_=next_,
        )
    ).parsed
