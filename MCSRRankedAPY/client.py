from aiohttp import ClientSession
from objects.match_info import MatchInfo
from objects.user_profile import UserProfile
from objects.versus_stats import VersusStats
from objects.leaderboards import EloLeaderboard, SeasonPhasePointsLeaderboard, BestTimeEntry, WeeklyRaceLeaderboard
from typing import Optional
from objects.exceptions import *

MCSR_RANKED_API_URI = "https://api.mcsrranked.com/"


class ClientSessionWrapper:
  def __init__(self, base_url: str):
    self._client = ClientSession(base_url=base_url)

  async def request_json(self, method: str, path: str, params: dict = {}) -> dict:
    async with self._client.request(method, path, params=params) as response:
      if response.status == 400:
        raise DataNotFoundException(path, params)

      json = await response.json()

      if response.status == 401:
        raise WrongParametersException(path, params, json.get("data"))
      elif response.status == 429:
        raise TooManyRequestsException(path, params, json.get("data"))

      return json

  async def close(self):
    await self._client.close()


class MCSRRankedClient:
  def __init__(self, key: Optional[str] = None):
    self._client = ClientSessionWrapper(base_url=MCSR_RANKED_API_URI)

    self.key = key
    self.users = Users(self._client)
    self.matches = Matches(self._client)
    self.leaderboards = Leaderboards(self._client)
    self.weekly_races = WeeklyRaces(self._client)

  async def close(self):
    await self._client.close()


class Users:
  def __init__(self, client: ClientSessionWrapper, key: str = None):
    self._client = client
    self.key = key

  async def get_data(self, identifier: str, **kwargs) -> UserProfile:
    json = await self._client.request_json(
        "GET", f"users/{identifier}", params=kwargs)
    data = json.get("data")
    return UserProfile(**data)

  async def get_matches(self, identifier: str, **kwargs) -> list[MatchInfo]:
    json = await self._client.request_json("GET", f"users/{identifier}/matches", params=kwargs)
    data = json.get("data")
    return [MatchInfo(**data[i]) for i in range(len(data))]

  async def get_versus_stats(self, identifier1: str, identifier2: str, **kwargs) -> VersusStats:
    json = await self._client.request_json("GET", f"users/{identifier1}/versus/{identifier2}", params=kwargs)
    data = json.get("data")
    versus_stats = VersusStats(**data)

    # this is bad API design in my opinion because the name of the field is dependent on the query, so this is a workaround method that uses a dict
    for i in range(2):
      versus_stats.results.ranked.per_player[versus_stats.players[i].uuid] = data.get(
          "results").get("ranked").get(versus_stats.players[i].uuid)
      versus_stats.results.casual.per_player[versus_stats.players[i].uuid] = data.get(
          "results").get("casual").get(versus_stats.players[i].uuid)

    return versus_stats

  async def get_seasons(self, identifier: str, **kwargs) -> UserProfile:
    json = await self._client.request_json("GET", f"users/{identifier}/seasons", params=kwargs)
    data = json.get("data")
    user_profile = UserProfile(**data)
    return user_profile


class Matches:
  def __init__(self, client: ClientSessionWrapper, key: str = None):
    self._client = client
    self.key = key

  async def get_recent(self, **kwargs) -> list[MatchInfo]:
    """Gets the basic information about recent matches"""
    json = await self._client.request_json("GET", "matches", params=kwargs)
    data = json.get("data")
    return [MatchInfo(**data[i]) for i in range(len(data))]

  async def get_info(self, id: int, **kwargs) -> MatchInfo:
    """Gets the advanced information about a specific match"""
    json = await self._client.request_json("GET", f"matches/{id}", params=kwargs)
    data = json.get("data")
    return MatchInfo(**data)


class Leaderboards:
  def __init__(self, client: ClientSessionWrapper, key: str = None):
    self._client = client
    self.key = key

  async def get_elo(self, **kwargs):
    """Gets the ELO leaderboard (top 150 but not always 150)"""
    json = await self._client.request_json("GET", "leaderboard", params=kwargs)
    data = json.get("data")
    return EloLeaderboard(**data)

  async def get_season_phase_points(self, **kwargs):
    """Gets the season phase points leaderboard"""
    json = await self._client.request_json("GET", "phase-leaderboard", params=kwargs)
    data = json.get("data")
    return SeasonPhasePointsLeaderboard(**data)

  async def get_season_phase_points(self, **kwargs):
    """Gets the season best time leaderboard"""
    json = await self._client.request_json("GET", "record-leaderboard", params=kwargs)
    data = json.get("data")
    return [BestTimeEntry(**data[i]) for i in range(len(data))]


class WeeklyRaces:
  def __init__(self, client: ClientSessionWrapper, key: str = None):
    self._client = client
    self.key = key

  async def get_info_leaderboard(self, id: int = -1, **kwargs):
    """Get weekly race info and leaderboard"""
    json = await self._client.request_json("GET", f"weekly-race{'' if id < 0 else f'/{id}'}")
    data = json.get("data")
    return WeeklyRaceLeaderboard(**data)
