from PySide6.QtCore import (
    QCoreApplication,
    QTimer,
)

from elmely.services.scheduler_service import SchedulerService


def callback():

    print("Scheduler callback")

    return True


app = QCoreApplication([])

scheduler = SchedulerService(
    retry_interval_ms=2000,
    hourly_interval_ms=5000,
)

scheduler.start(callback)

#
# Avslutt testen etter 20 sekunder.
#

QTimer.singleShot(
    20_000,
    app.quit,
)

app.exec()

print("Scheduler test finished")