from __future__ import annotations
from pydantic import BaseModel, Field
from datetime import datetime, timedelta
from typing import Optional, List, Dict


class Achievement(BaseModel):
  id: str
  date: datetime
  data: List[str]
  level: int
  goal: Optional[int] = None


class Achievements(BaseModel):
  display: List
  total: List[Achievement]


class Timestamp(BaseModel):
  firstOnline: Optional[datetime] = None
  lastOnline: Optional[datetime] = None
  lastRanked: Optional[datetime] = None
  nextDecay: Optional[datetime] = None


class StatisticsBestTime(BaseModel):
  ranked: Optional[timedelta] = None
  casual: Optional[timedelta] = None


class StatisticsHighestWinStreak(BaseModel):
  ranked: Optional[int] = None
  casual: Optional[int] = None


class StatisticsCurrentWinStreak(BaseModel):
  ranked: Optional[int] = None
  casual: Optional[int] = None


class StatisticsPlayedMatches(BaseModel):
  ranked: Optional[timedelta] = None
  casual: Optional[timedelta] = None


class StatisticsPlaytime(BaseModel):
  ranked: Optional[timedelta] = None
  casual: Optional[timedelta] = None


class StatisticsCompletionTime(BaseModel):
  ranked: Optional[timedelta] = None
  casual: Optional[timedelta] = None


class StatisticsForfeits(BaseModel):
  ranked: Optional[int] = None
  casual: Optional[int] = None


class StatisticsCompletions(BaseModel):
  ranked: Optional[int] = None
  casual: Optional[int] = None


class StatisticsWins(BaseModel):
  ranked: Optional[int] = None
  casual: Optional[int] = None


class StatisticsLosses(BaseModel):
  ranked: Optional[int] = None
  casual: Optional[int] = None


class StatisticsEntry(BaseModel):
  bestTime: StatisticsBestTime
  highestWinStreak: StatisticsHighestWinStreak
  currentWinStreak: StatisticsCurrentWinStreak
  playedMatches: StatisticsPlayedMatches
  playtime: StatisticsPlaytime
  completionTime: StatisticsCompletionTime
  forfeits: StatisticsForfeits
  completions: StatisticsCompletions
  wins: StatisticsWins
  loses: StatisticsLosses


class Statistics(BaseModel):
  season: StatisticsEntry
  total: StatisticsEntry


class ConnectionsEntry(BaseModel):
  id: str
  name: str


class Connections(BaseModel):
  youtube: Optional[ConnectionsEntry] = None
  twitch: Optional[ConnectionsEntry] = None
  discord: Optional[ConnectionsEntry] = None


class WeeklyRace(BaseModel):
  id: int
  time: timedelta
  rank: int


class SeasonResultLast(BaseModel):
  eloRate: Optional[int] = None
  eloRank: Optional[int] = None
  phasePoint: Optional[int] = None


class SeasonResultPhase(BaseModel):
  phase: Optional[int] = None
  eloRate: Optional[int] = None
  eloRank: Optional[int] = None
  point: Optional[int] = None


class SeasonResult(BaseModel):
  last: SeasonResultLast
  highest: Optional[int] = None
  lowest: Optional[int] = None
  phases: List[SeasonResultPhase] = Field(default_factory=list)


class UserProfile(BaseModel):
  uuid: str
  nickname: str
  roleType: int
  eloRate: Optional[int] = None
  eloRank: Optional[int] = None
  country: Optional[str] = None
  achievements: Optional[Achievements] = None
  timestamp: Optional[Timestamp] = None
  statistics: Optional[Statistics] = None
  connections: Optional[Connections] = None
  weeklyRaces: List[WeeklyRace] = Field(default_factory=list)
  seasonPlaced: Optional[bool] = None
  seasonResult: Optional[SeasonResult] = None
  seasonResults: Optional[Dict[str, SeasonResult]] = None
