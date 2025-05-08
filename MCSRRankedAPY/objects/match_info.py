from __future__ import annotations
from pydantic import BaseModel, Field
from datetime import datetime, timedelta
from typing import List, Optional
from enum import Enum
from .user_profile import UserProfile

class MatchType(Enum):
    CASUAL = 1
    RANKED = 2
    PRIVATE_ROOM = 3
    EVENT_MODE = 4

class Seed(BaseModel):
    id: Optional[str] = None
    overworld: Optional[str] = None
    bastion: Optional[str] = None
    endTowers: List[int] = Field(default_factory=list)
    variations: List[str] = Field(default_factory=list)

class Result(BaseModel):
    uuid: Optional[str] = None
    time: timedelta

class Rank(BaseModel):
    season: Optional[int] = None
    allTime: Optional[int] = None

class Changes(BaseModel):
    uuid: str
    change: Optional[int] = None
    eloRate: Optional[int] = None

class Advanced(BaseModel):
    # Placeholder for future fields
    pass

class MatchInfo(BaseModel):
    id: int
    type: MatchType
    season: int
    category: str
    date: datetime
    players: List[UserProfile] = Field(default_factory=list)
    spectators: List[UserProfile] = Field(default_factory=list)
    seed: Seed
    result: Result
    forfeited: bool
    decayed: bool
    rank: Rank
    changes: List[Changes] = Field(default_factory=list)
    tag: Optional[str] = None