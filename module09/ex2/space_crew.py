from pydantic import BaseModel, ValidationError, model_validator, Field
from datetime import datetime
from enum import Enum


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(gt=0, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1, le=10000)

    def is_commander_captain(self) -> bool:
        for member in self.crew:
            if member.rank == Rank.COMMANDER or member.rank == Rank.CAPTAIN:
                return True
        return False

    def is_crew_experienced(self) -> bool:
        crew_size: int = len(self.crew)
        experienced_members: int = 0
        experienced_members += sum(1 for memb in self.crew if memb.years_experience > 5)
        return experienced_members >= crew_size / 2

    def crew_active(self) -> bool:
        return all(memb.is_active for memb in self.crew)

    @model_validator(mode='after')
    def mission_rules(self) -> "SpaceMission":
        if self.mission_id[:1] != "M":
            return ValueError("Mission ID must start with 'M'")
        if not self.is_commander_captain():
            return ValueError("Mission must have at least one Commander or Captain")
        if self.duration_days > 365 and not self.is_crew_experienced():
            return ValueError("Long missions (> 365 days) need 50% experienced crew (5+ years)")
        if not self.crew_active():
            return ValueError("All crew members must be active")
        return self


def main() -> None:
    print("Space Mission Crew Validation")


if __name__ == "__main__":
    main()