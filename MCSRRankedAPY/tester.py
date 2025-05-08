from src.client import MCSRRankedClient
from pprint import pprint

import asyncio

async def main():
  api = MCSRRankedClient()
  query = await api.users.get_user_matches("xiaomyer")
  pprint(query)

if __name__ == "__main__":
  asyncio.run(main())