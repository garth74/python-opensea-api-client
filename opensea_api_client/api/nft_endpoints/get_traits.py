from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_trait_response import GetTraitResponse
from ...types import Response


def _get_kwargs(
    collection_slug: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2/traits/{collection_slug}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetTraitResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetTraitResponse.from_dict(response.json())

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
) -> Response[Union[Any, GetTraitResponse]]:
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
) -> Response[Union[Any, GetTraitResponse]]:
    """Get Traits

     Get the traits in a collection.

    Args:
        collection_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetTraitResponse]]
    """

    kwargs = _get_kwargs(
        collection_slug=collection_slug,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    collection_slug: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, GetTraitResponse]]:
    """Get Traits

     Get the traits in a collection.

    Args:
        collection_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetTraitResponse]
    """

    return sync_detailed(
        collection_slug=collection_slug,
        client=client,
    ).parsed


async def asyncio_detailed(
    collection_slug: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, GetTraitResponse]]:
    """Get Traits

     Get the traits in a collection.

    Args:
        collection_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetTraitResponse]]
    """

    kwargs = _get_kwargs(
        collection_slug=collection_slug,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collection_slug: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, GetTraitResponse]]:
    """Get Traits

     Get the traits in a collection.

    Args:
        collection_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetTraitResponse]
    """

    return (
        await asyncio_detailed(
            collection_slug=collection_slug,
            client=client,
        )
    ).parsed
