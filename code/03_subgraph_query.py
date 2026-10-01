#!/usr/bin/env python3
"""Example Subgraph GraphQL query for Uniswap V3."""

QUERY = """
query PoolMetrics($pool: String!, $skip: Int!) {
  pools(where: { id: $pool }, first: 1) {
    id
    token0 { symbol }
    token1 { symbol }
    feeTier
    liquidity
    txCount
    volumeUSD
    totalValueLockedUSD
    ticks(first: 5, skip: $skip) {
      tickIdx
      liquidityGross
      liquidityNet
    }
  }
}
"""


def main():
    print("=== Example Subgraph Query ===")
    print(QUERY)
    print("\nSuggested variables:")
    print("{")
    print('  "pool": "0x8ad599c3a0ff1de082011efddc58f1908eb6e6d8",')
    print('  "skip": 0')
    print("}")


if __name__ == "__main__":
    main()
