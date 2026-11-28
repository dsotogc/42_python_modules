from pydantic import BaseModel, Field, model_validator, ValidationError
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
    def check_contact_id(self) -> "AlienContact":
        if self.contact_id[:2] != "AC":
            raise ValueError("Contact ID must start with 'AC'")
        return self

    @model_validator(mode='after')
    def physical_verified(self) -> "AlienContact":
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        return self

    @model_validator(mode='after')
    def telepathic_witness_check(self) -> "AlienContact":
        if (
            self.contact_type == ContactType.TELEPATHIC
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )
        return self

    @model_validator(mode='after')
    def strong_signal_check(self) -> "AlienContact":
        if self.signal_strength > 7 and not self.message_received:
            raise ValueError(
                "Strong signals (> 7.0) should include received messages"
            )
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
        print(f"Type: {ac.contact_type.value}")
        print(f"Location: {ac.location}")
        print(f"Signal: {ac.signal_strength}/10")
        print(f"Duration: {ac.duration_minutes} minutes")
        print(f"Witnesses: {ac.witness_count}")
        print(f"Message: {ac.message_received}")
    except ValidationError as e:
        print(e)
    print()
    print("===================================")
    print("Expected validation error:")
    try:
        ac_failed: AlienContact = AlienContact(
            contact_id="AC_2026_042",
            timestamp=datetime.now(),
            location="Majadahonda",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=6.5,
            duration_minutes=42,
            witness_count=2,
            message_received="Whatsapp 2"
        )
        print(f"ID: {ac_failed.contact_id}")
        print(f"Type: {ac_failed.contact_type.value}")
        print(f"Location: {ac_failed.location}")
        print(f"Signal: {ac_failed.signal_strength}/10")
        print(f"Duration: {ac_failed.duration_minutes} minutes")
        print(f"Witnesses: {ac_failed.witness_count}")
        print(f"Message: {ac_failed.message_received}")
    except ValidationError as e:
        print(e.errors()[0]['msg'])


if __name__ == "__main__":
    main()
