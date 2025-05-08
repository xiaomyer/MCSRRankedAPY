from __future__ import annotations
from pydantic import BaseModel, Field
from datetime import datetime, timedelta
from typing import Optional, List

from .user_profile import UserProfile


class VersusStatsResultsEntry(BaseModel):
  total: int
  per_player: dict = Field(default_factory=dict)


class VersusStatsResults(BaseModel):
  ranked: VersusStatsResultsEntry
  casual: VersusStatsResultsEntry


class VersusStats(BaseModel):
  players: List[UserProfile]
  results: VersusStatsResults
