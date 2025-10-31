"""Copyright (C) 2021-2024 Katelynn Cadwallader.

This file is part of GarlandToolsAPI_wrapper.

GarlandToolsAPI_wrapper is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3, or (at your option)
any later version.

GarlandToolsAPI_wrapper is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public
License for more details.

You should have received a copy of the GNU General Public License
along with GarlandToolsAPI_wrapper; see the file COPYING.  If not, write to the Free
Software Foundation, 51 Franklin Street - Fifth Floor, Boston, MA
02110-1301, USA.
"""

import logging

__all__ = ("GarlandToolsKeyError", "GarlandToolsRequestError", "GarlandToolsTypeError")

LOGGER = logging.getLogger("async_garlandtools.errors")


class GarlandToolsRequestError(Exception):  # noqa: D101
    def __init__(self, status_code: int, url: str, error_reason: str) -> None:  # noqa: D107
        message = "We encountered an error during a request to GarlandTools in %s. Current URL: %r | Status Code: %s"
        super().__init__(message, error_reason, url, status_code)
        LOGGER.error(message, error_reason, url, status_code)


class GarlandToolsKeyError(Exception):  # noqa: D101
    def __init__(self, key_name: str, func: str, *args: object) -> None:  # noqa: D107
        message = "We encountered an KeyError in our response data from GarlandTools in %s. | Missing Key Name: %s | Args: %s"
        super().__init__(message, func, key_name, *args)
        LOGGER.error(message, func, key_name, *args)


class GarlandToolsTypeError(Exception):  # noqa: D101
    def __init__(self, func: str, cur_type: object, expec_type: object) -> None:  # noqa: D107
        message = "We encountered a TypeError, the response data from GarlandTools is invalid in %s. | Response: %s | Expected: %s"
        super().__init__(message, func, cur_type.__class__.__name__, expec_type.__class__.__name__)
