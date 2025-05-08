# MCSRRankedAPY - MCSR Ranked Statistics API Wrapper

Asynchronous wrapper for the MCSRRanked API

## Features
- Full API coverage (API key usage not yet tested)

## Installation
`mcsrrankedapy` is available from the official PyPI package index.

`python -m pip install -U mcsrrankedapy`

## Documentation

https://docs.mcsrranked.com/

The wrapper is almost 100% 1-to-1 consistent with the original JSON API. The only inconsistency is in the `.users.get_versus_stats` method. The API returns data with keys that depend on the query, which is unpythonic to implement in a Pydantic model. The wrapper instead creates a `dict` named `per_player` that matches the API's response.

The official MCSR Ranked API docs describe what specific fields get returned from specific endpoints.

## Quick Start
```py
from mcsrrankedapy import MCSRRankedAPYClient
import asyncio


async def main():
  client = MCSRRankedAPYClient()
  query = await client.users.get_data("lowk3y_")
  print(query.connections.youtube.id) # prints UC_HX7WdiAWRZgcG7aOYtCNg
  await client.close()

if __name__ == "__main__":
  asyncio.run(main())
```
