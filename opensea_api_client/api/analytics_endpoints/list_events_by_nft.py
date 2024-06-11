from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_events_by_nft_chain import ListEventsByNftChain
from ...models.list_events_by_nft_event_type_item import ListEventsByNftEventTypeItem
from ...models.list_events_response import ListEventsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    chain: ListEventsByNftChain,
    address: str,
    identifier: str,
    *,
    after: Union[Unset, float] = UNSET,
    before: Union[Unset, float] = UNSET,
    event_type: Union[Unset, List[ListEventsByNftEventTypeItem]] = UNSET,
    next_: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["after"] = after

    params["before"] = before

    json_event_type: Union[Unset, List[str]] = UNSET
    if not isinstance(event_type, Unset):
        json_event_type = []
        for event_type_item_data in event_type:
            event_type_item = event_type_item_data.value
            json_event_type.append(event_type_item)

    params["event_type"] = json_event_type

    params["next"] = next_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2/events/chain/{chain}/contract/{address}/nfts/{identifier}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ListEventsResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ListEventsResponse.from_dict(response.json())

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
) -> Response[Union[Any, ListEventsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    chain: ListEventsByNftChain,
    address: str,
    identifier: str,
    *,
    client: AuthenticatedClient,
    after: Union[Unset, float] = UNSET,
    before: Union[Unset, float] = UNSET,
    event_type: Union[Unset, List[ListEventsByNftEventTypeItem]] = UNSET,
    next_: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ListEventsResponse]]:
    """Get Events (by NFT)

     Get a list of events for a single NFT. The list will be paginated and include up to 100 events per
    page.

    Args:
        chain (ListEventsByNftChain):
        address (str):
        identifier (str):
        after (Union[Unset, float]):
        before (Union[Unset, float]):
        event_type (Union[Unset, List[ListEventsByNftEventTypeItem]]):
        next_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ListEventsResponse]]
    """

    kwargs = _get_kwargs(
        chain=chain,
        address=address,
        identifier=identifier,
        after=after,
        before=before,
        event_type=event_type,
        next_=next_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    chain: ListEventsByNftChain,
    address: str,
    identifier: str,
    *,
    client: AuthenticatedClient,
    after: Union[Unset, float] = UNSET,
    before: Union[Unset, float] = UNSET,
    event_type: Union[Unset, List[ListEventsByNftEventTypeItem]] = UNSET,
    next_: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ListEventsResponse]]:
    """Get Events (by NFT)

     Get a list of events for a single NFT. The list will be paginated and include up to 100 events per
    page.

    Args:
        chain (ListEventsByNftChain):
        address (str):
        identifier (str):
        after (Union[Unset, float]):
        before (Union[Unset, float]):
        event_type (Union[Unset, List[ListEventsByNftEventTypeItem]]):
        next_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ListEventsResponse]
    """

    return sync_detailed(
        chain=chain,
        address=address,
        identifier=identifier,
        client=client,
        after=after,
        before=before,
        event_type=event_type,
        next_=next_,
    ).parsed


async def asyncio_detailed(
    chain: ListEventsByNftChain,
    address: str,
    identifier: str,
    *,
    client: AuthenticatedClient,
    after: Union[Unset, float] = UNSET,
    before: Union[Unset, float] = UNSET,
    event_type: Union[Unset, List[ListEventsByNftEventTypeItem]] = UNSET,
    next_: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ListEventsResponse]]:
    """Get Events (by NFT)

     Get a list of events for a single NFT. The list will be paginated and include up to 100 events per
    page.

    Args:
        chain (ListEventsByNftChain):
        address (str):
        identifier (str):
        after (Union[Unset, float]):
        before (Union[Unset, float]):
        event_type (Union[Unset, List[ListEventsByNftEventTypeItem]]):
        next_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ListEventsResponse]]
    """

    kwargs = _get_kwargs(
        chain=chain,
        address=address,
        identifier=identifier,
        after=after,
        before=before,
        event_type=event_type,
        next_=next_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    chain: ListEventsByNftChain,
    address: str,
    identifier: str,
    *,
    client: AuthenticatedClient,
    after: Union[Unset, float] = UNSET,
    before: Union[Unset, float] = UNSET,
    event_type: Union[Unset, List[ListEventsByNftEventTypeItem]] = UNSET,
    next_: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ListEventsResponse]]:
    """Get Events (by NFT)

     Get a list of events for a single NFT. The list will be paginated and include up to 100 events per
    page.

    Args:
        chain (ListEventsByNftChain):
        address (str):
        identifier (str):
        after (Union[Unset, float]):
        before (Union[Unset, float]):
        event_type (Union[Unset, List[ListEventsByNftEventTypeItem]]):
        next_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ListEventsResponse]
    """

    return (
        await asyncio_detailed(
            chain=chain,
            address=address,
            identifier=identifier,
            client=client,
            after=after,
            before=before,
            event_type=event_type,
            next_=next_,
        )
    ).parsed
