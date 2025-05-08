import aiohttp

from .objects.match_info import *
from .objects.user_profile import *

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