from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.detailed_account_data_model import DetailedAccountDataModel
from ...types import Response


def _get_kwargs(
    address: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2/accounts/{address}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, DetailedAccountDataModel]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DetailedAccountDataModel.from_dict(response.json())

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
) -> Response[Union[Any, DetailedAccountDataModel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    address: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, DetailedAccountDataModel]]:
    """Get Account

     Get an OpenSea Account Profile including details such as bio, social media usernames, and profile
    image.

    Args:
        address (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DetailedAccountDataModel]]
    """

    kwargs = _get_kwargs(
        address=address,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    address: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, DetailedAccountDataModel]]:
    """Get Account

     Get an OpenSea Account Profile including details such as bio, social media usernames, and profile
    image.

    Args:
        address (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DetailedAccountDataModel]
    """

    return sync_detailed(
        address=address,
        client=client,
    ).parsed


async def asyncio_detailed(
    address: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, DetailedAccountDataModel]]:
    """Get Account

     Get an OpenSea Account Profile including details such as bio, social media usernames, and profile
    image.

    Args:
        address (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DetailedAccountDataModel]]
    """

    kwargs = _get_kwargs(
        address=address,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    address: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, DetailedAccountDataModel]]:
    """Get Account

     Get an OpenSea Account Profile including details such as bio, social media usernames, and profile
    image.

    Args:
        address (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DetailedAccountDataModel]
    """

    return (
        await asyncio_detailed(
            address=address,
            client=client,
        )
    ).parsed
