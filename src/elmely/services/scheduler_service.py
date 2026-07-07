from __future__ import annotations

from datetime import datetime, timedelta
from typing import Callable

from PySide6.QtCore import QObject, QTimer

from elmely.core.logger import log


class SchedulerService(QObject):
    """
    Planlegger oppdateringer av dashboardet.

    Ved oppstart utføres en umiddelbar oppdatering via force_update().

    Deretter planlegges første automatiske oppdatering til
    ett minutt over neste hele time.

    Callback skal returnere:

        True  -> oppdateringen var vellykket

        False -> data var ikke klare ennå, prøv igjen om
                 30 sekunder.
    """

    RETRY_INTERVAL_MS = 30 * 1000
    HOURLY_INTERVAL_MS = 60 * 60 * 1000

    def __init__(
        self,
        retry_interval_ms: int = 30_000,
        hourly_interval_ms: int = 3_600_000,
    ):

        super().__init__()

        self._callback: Callable[[], bool] | None = None

        self._timer = QTimer(self)
        self._timer.setSingleShot(True)
        self._timer.timeout.connect(self._run_callback)
        self._retry_interval_ms = retry_interval_ms
        self._hourly_interval_ms = hourly_interval_ms

    def start(
        self,
        callback: Callable[[], bool],
    ):

        self._callback = callback

        log.info("Scheduler started")

        self._schedule_next_update()
        #
        # Oppdater med én gang.
        #

        ok = self._callback()

        if ok:

            self._schedule_next_update()

        else:

            self._schedule_retry()
            
    def stop(self):

        self._timer.stop()

        log.info("Scheduler stopped")

    def force_update(self):

        if self._callback is None:
            return

        log.info("Forced dashboard update")

        ok = self._callback()

        if ok:

            self._schedule_next_update()

        else:

            self._schedule_retry()

    #
    # Intern logikk
    #

    def _run_callback(self):

        if self._callback is None:
            return

        log.info("Running scheduled update")

        ok = self._callback()

        if ok:

            self._schedule_hourly_update()

        else:

            self._schedule_retry()

    def _schedule_retry(self):

        log.info("Update not ready, retry in 30 seconds")

        self._timer.start(
            self._retry_interval_ms
        )

    def _schedule_hourly_update(self):

        log.info("Next update in one hour")

        self._timer.start(
            self._hourly_interval_ms
        )

    def _schedule_next_update(self):

        now = datetime.now()

        next_update = now.replace(
            minute=1,
            second=0,
            microsecond=0,
        )

        if now.minute >= 1:

            next_update += timedelta(hours=1)

        delay = int(
            (
                next_update - now
            ).total_seconds()
            * 1000
        )

        log.info(

            "Next scheduled update: "

            f"{next_update:%H:%M:%S}"

        )

        self._timer.start(delay)