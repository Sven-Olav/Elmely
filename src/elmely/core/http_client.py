from __future__ import annotations

import requests

from elmely.core.logger import log


class HttpClient:

    DEFAULT_TIMEOUT = 15

    def get_json(
        self,
        url: str,
        params: dict | None = None,
    ) -> dict:

        log.info(f"HTTP GET {url}")

        response = requests.get(
            url,
            params=params,
            timeout=self.DEFAULT_TIMEOUT,
            headers={
                "User-Agent": "Elmely Energy Monitor",
            },
        )

        response.raise_for_status()

        log.info(
            f"HTTP {response.status_code} "
            f"({len(response.content)} bytes)"
        )

        return response.json()