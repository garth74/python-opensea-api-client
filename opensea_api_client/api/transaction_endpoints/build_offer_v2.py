from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.build_offer import BuildOffer
from ...models.build_offer_input import BuildOfferInput
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        BuildOfferInput,
        BuildOfferInput,
        BuildOfferInput,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/offers/build",
    }

    if isinstance(body, BuildOfferInput):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, BuildOfferInput):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, BuildOfferInput):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, BuildOffer]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = BuildOffer.from_dict(response.json())

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
) -> Response[Union[Any, BuildOffer]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        BuildOfferInput,
        BuildOfferInput,
        BuildOfferInput,
    ],
) -> Response[Union[Any, BuildOffer]]:
    """Build an Offer

     Build a portion of a criteria offer including the merkle tree needed to post an offer.

    Args:
        body (BuildOfferInput):
        body (BuildOfferInput):
        body (BuildOfferInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BuildOffer]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: Union[
        BuildOfferInput,
        BuildOfferInput,
        BuildOfferInput,
    ],
) -> Optional[Union[Any, BuildOffer]]:
    """Build an Offer

     Build a portion of a criteria offer including the merkle tree needed to post an offer.

    Args:
        body (BuildOfferInput):
        body (BuildOfferInput):
        body (BuildOfferInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BuildOffer]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        BuildOfferInput,
        BuildOfferInput,
        BuildOfferInput,
    ],
) -> Response[Union[Any, BuildOffer]]:
    """Build an Offer

     Build a portion of a criteria offer including the merkle tree needed to post an offer.

    Args:
        body (BuildOfferInput):
        body (BuildOfferInput):
        body (BuildOfferInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BuildOffer]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: Union[
        BuildOfferInput,
        BuildOfferInput,
        BuildOfferInput,
    ],
) -> Optional[Union[Any, BuildOffer]]:
    """Build an Offer

     Build a portion of a criteria offer including the merkle tree needed to post an offer.

    Args:
        body (BuildOfferInput):
        body (BuildOfferInput):
        body (BuildOfferInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BuildOffer]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
