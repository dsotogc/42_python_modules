from pydantic import BaseModel, Field, model_validator, ValidationError
from typing import Self
from enum import Enum
from datetime import datetime


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0, le=10)
    duration_minutes: int = Field(gt=0, le=1440)
    witness_count: int = Field(gt=0, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def check_contact_id(self) -> Self:
        if self.contact_id[:2] != "AC":
            raise ValueError("Contact ID must start with 'AC'")
        return self

    @model_validator(mode='after')
    def physical_verified(self) -> Self:
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        return self

    @model_validator(mode='after')
    def telepathic_witness_check(self) -> Self:
        if self.contact_type == ContactType.TELEPATHIC and self.witness_count < 3:
            raise ValueError("Telepathic contact requires at least 3 witnesses")
        return self

    @model_validator(mode='after')
    def strong_signal_check(self) -> Self:
        if self.signal_strength > 7 and not self.message_received:
            raise ValueError("Strong signals (> 7.0) should include received messages")
        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("===================================")
    print("Valid contact report:")
    try:
        ac: AlienContact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.RADIO,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli"
        )
        print(f"ID: {ac.contact_id}")
        print(f"Type: {ac.contact_type}")
    except ValidationError
