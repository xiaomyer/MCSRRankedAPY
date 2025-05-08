from client import MCSRRankedClient
from pprint import pprint

import asyncio


async def main():
  try:
    api = MCSRRankedClient()
    query = await api.matches.get_info(2076243)
    # query = await api.matches.get_recent()
    pprint(query)
  finally:
    await api.close()

if __name__ == "__main__":
  asyncio.run(main())
