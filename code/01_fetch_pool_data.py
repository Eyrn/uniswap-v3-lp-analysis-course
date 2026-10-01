#!/usr/bin/env python3
"""Fetch and display sample pool data for Uniswap V3 LP analysis."""

import json
from pathlib import Path


def load_pool_data(path: str | None = None):
    default_path = Path(__file__).resolve().parents[1] / "data" / "sample_pools.json"
    target = Path(path) if path else default_path
    with target.open("r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def main():
    pool = load_pool_data()
    print("=== Uniswap V3 Pool Overview ===")
    print(f"Pool Address: {pool['address']}")
    print(f"Pair: {pool['token0']} / {pool['token1']}")
    print(f"Fee: {pool['fee']}%")
    print(f"Current Price: {pool['sqrtPriceX96']} (sqrtPriceX96)")
    print(f"Liquidity: {pool['liquidity']}")
    print(f"Tick: {pool['tick']}")
    print(f"TVL: ${pool['tvl_usd']:,.0f}")
    print(f"24h Volume: ${pool['volume_24h_usd']:,.0f}")

    print("\nPool fields:")
    for key in ["sqrtPriceX96", "tick", "liquidity", "fee", "token0", "token1"]:
        print(f"  - {key}: {pool[key]}")


if __name__ == "__main__":
    main()
