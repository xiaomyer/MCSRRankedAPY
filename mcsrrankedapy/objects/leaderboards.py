from pydantic import BaseModel, Field
from datetime import datetime, timedelta
from typing import List

from .user_profile import UserProfile


class Season(BaseModel):
  endsAt: datetime
  number: int


class EloLeaderboard(BaseModel):
  season: Season
  users: List[UserProfile] = Field(default_factory=list)


class Phase(BaseModel):
  endsAt: datetime
  number: int
  season: int


class SeasonPhasePointsLeaderboard(BaseModel):
  phase: Phase
  users: List[UserProfile] = Field(default_factory=list)


class BestTimeEntry(BaseModel):
  rank: int
  season: int
  date: datetime
  id: int
  time: timedelta
  user: UserProfile


# class BestTimeLeaderboard(BaseModel):


class WeeklyRaceEntry(BaseModel):
  rank: int
  player: UserProfile
  time: timedelta
  replayExist: bool


class WeeklyRaceSeed(BaseModel):
  overworld: str
  nether: str
  theEnd: str
  rng: str


class WeeklyRaceLeaderboard(BaseModel):
  id: int
  seed: WeeklyRaceSeed
  endsAt: datetime
  leaderboard: List[WeeklyRaceEntry] = Field(default_factory=list)
