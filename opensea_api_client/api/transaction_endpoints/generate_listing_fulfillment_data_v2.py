from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.generate_listing_fulfillment_input import GenerateListingFulfillmentInput
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        GenerateListingFulfillmentInput,
        GenerateListingFulfillmentInput,
        GenerateListingFulfillmentInput,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/listings/fulfillment_data",
    }

    if isinstance(body, GenerateListingFulfillmentInput):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, GenerateListingFulfillmentInput):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, GenerateListingFulfillmentInput):
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
    *,
    client: AuthenticatedClient,
    body: Union[
        GenerateListingFulfillmentInput,
        GenerateListingFulfillmentInput,
        GenerateListingFulfillmentInput,
    ],
) -> Response[Any]:
    """Fulfill a Listing

     Retrieve all the information, including signatures, needed to fulfill a listing directly onchain.

    Args:
        body (GenerateListingFulfillmentInput):
        body (GenerateListingFulfillmentInput):
        body (GenerateListingFulfillmentInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        GenerateListingFulfillmentInput,
        GenerateListingFulfillmentInput,
        GenerateListingFulfillmentInput,
    ],
) -> Response[Any]:
    """Fulfill a Listing

     Retrieve all the information, including signatures, needed to fulfill a listing directly onchain.

    Args:
        body (GenerateListingFulfillmentInput):
        body (GenerateListingFulfillmentInput):
        body (GenerateListingFulfillmentInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
