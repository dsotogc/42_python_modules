from datetime import datetime
from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0, le=100)
    oxygen_level: float = Field(ge=0, le=100)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: str | None = Field(default=None, max_length=200)

    def print_info(self) -> None:
        print("Valid station created:")
        print(f"ID: {self.station_id}")
        print(f"Name: {self.name}")
        print(f"Crew: {self.crew_size} people")
        print(f"Power: {self.power_level}%")
        print(f"Oxygen: {self.oxygen_level}%")
        print(f"Status: {'Operational' if self.is_operational else 'Offline'}")


def main() -> None:
    print("Space Station Data Validation")
    print("=======================================")
    station: SpaceStation = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=95.3,
        last_maintenance=datetime.now()
    )
    station.print_info()
    print("\n=======================================")
    print("Expected validation error:")
    try:
        failed_station: SpaceStation = SpaceStation(
            station_id="ISS002",
            name="Crowded Station",
            crew_size=320,
            power_level=10.5,
            oxygen_level=90.0,
            last_maintenance=datetime.now()
        )
        failed_station.print_info()
    except ValidationError as e:
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()
