"""Candidate-facing API data models."""

from pydantic import BaseModel, ConfigDict, Field


class CandidateProfile(BaseModel):
    """Validated representation of a candidate's career profile.

    This model intentionally contains no persistence or agent-specific logic;
    it is the shared contract for future API and service layers.
    """

    model_config = ConfigDict(str_strip_whitespace=True)

    name: str = Field(min_length=1, description="Candidate's full name.")
    email: str = Field(min_length=1, description="Candidate's email address.")
    phone: str = Field(min_length=1, description="Candidate's phone number.")
    experience_years: float = Field(
        ge=0,
        description="Total professional experience in years.",
    )
    skills: list[str] = Field(description="Candidate's professional skills.")
    certifications: list[str] = Field(description="Candidate's certifications.")
    preferred_roles: list[str] = Field(
        description="Roles the candidate is interested in pursuing."
    )
