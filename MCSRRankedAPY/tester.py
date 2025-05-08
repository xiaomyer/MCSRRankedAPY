from client import MCSRRankedClient
from pprint import pprint

import asyncio


async def main():
  api = MCSRRankedClient()
  query = await api.users.get_versus_stats("doogile", "lowk3y_")
  pprint(query)

if __name__ == "__main__":
  asyncio.run(main())
