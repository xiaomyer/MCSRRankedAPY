from __future__ import annotations
from pydantic import BaseModel, Field
from datetime import datetime, timedelta
from typing import Optional, List

from user_profile import UserProfile

# class VersusStatsResults(BaseModel):

class VersusStats(BaseModel):
  players: List[UserProfile]
  # results:
