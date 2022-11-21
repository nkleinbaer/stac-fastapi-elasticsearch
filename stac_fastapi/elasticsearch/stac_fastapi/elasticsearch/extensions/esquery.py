"""ES Query Extension."""
from typing import Any, Dict, List, Optional

import attr
from fastapi import FastAPI
from pydantic import BaseModel

from stac_fastapi.types.extension import ApiExtension
from stac_fastapi.types.search import APIRequest


@attr.s
class ESQueryExtensionGetRequest(APIRequest):
    """Query Extension GET request model."""

    esquery: Optional[str] = attr.ib(default=None)


class ESQueryExtensionPostRequest(BaseModel):
    """Query Extension POST request model."""

    esquery: Optional[Dict[str, Dict[str, Any]]]


@attr.s
class ESQueryExtension(ApiExtension):
    """Query Extension.

    The Query extension adds an additional `esquery` parameter to `/search` requests which allows the caller to perform
    queries against item metadata (ex. find all images with cloud cover less than 15%).

    https://github.com/radiantearth/stac-api-spec/blob/master/item-search/README.md#query
    """

    GET = ESQueryExtensionGetRequest
    POST = ESQueryExtensionPostRequest

    conformance_classes: List[str] = attr.ib(factory=lambda: [""])
    schema_href: Optional[str] = attr.ib(default=None)

    def register(self, app: FastAPI) -> None:
        """Register the extension with a FastAPI application.

        Args:
            app: target FastAPI application.

        Returns:
            None
        """
        pass
