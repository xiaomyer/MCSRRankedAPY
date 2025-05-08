import aiohttp

from objects.match_info import MatchInfo
from objects.user_profile import UserProfile
from objects.versus_stats import VersusStats

MCSR_RANKED_API_URI = "https://api.mcsrranked.com"


class MCSRRankedClient:
  def __init__(self, key: str = None):
    self.key = key
    self.users = Users()


class Users:
  def __init__(self, key: str = None):
    self.key = key

  async def get_user_data(self, identifier: str, **kwargs):
    async with aiohttp.request("GET", f"{MCSR_RANKED_API_URI}/users/{identifier}", params=kwargs) as response:
      data = await response.json()
      data = data.get("data")
      return UserProfile(**data)

  async def get_user_matches(self, identifier: str, **kwargs):
    async with aiohttp.request("GET", f"{MCSR_RANKED_API_URI}/users/{identifier}/matches", params=kwargs) as response:
      data = await response.json()
      data = data.get("data")
      return [MatchInfo(**data[i]) for i in range(len(data))]

  async def get_versus_stats(self, identifier1: str, identifier2: str, **kwargs):
    async with aiohttp.request("GET", f"{MCSR_RANKED_API_URI}/users/{identifier1}/versus/{identifier2}", params=kwargs) as response:
      data = await response.json()
      data = data.get("data")
      versus_stats = VersusStats(**data)

      # this is bad API design in my opinion because the name of the field is dependent on the query, so this is a workaround method that uses a dict
      for i in range(2):
        versus_stats.results.ranked.per_player[versus_stats.players[i].uuid] = data.get(
            "results").get("ranked").get(versus_stats.players[i].uuid)
        versus_stats.results.casual.per_player[versus_stats.players[i].uuid] = data.get(
            "results").get("casual").get(versus_stats.players[i].uuid)

      return versus_stats
