from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Airport:
    code: str
    name: str


@dataclass(frozen=True)
class Aircraft:
    registration: str
    aircraft_type: str


@dataclass(frozen=True)
class Flight:
    flight_number: str
    aircraft: Aircraft
    origin: Airport
    destination: Airport
    scheduled_departure: datetime
    scheduled_arrival: datetime

    @property
    def duration_minutes(self) -> int:
        duration = self.scheduled_arrival - self.scheduled_departure
        return int(duration.total_seconds() / 60)
