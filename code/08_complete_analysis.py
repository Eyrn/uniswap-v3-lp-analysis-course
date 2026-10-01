#!/usr/bin/env python3
"""Provide a complete entry point for sample LP analysis."""

from pathlib import Path

from code import 01_fetch_pool_data


def main():
    print("=== Uniswap V3 LP Analysis Demo ===")
    pool = 01_fetch_pool_data.load_pool_data()
    print(f"Pool: {pool['token0']} / {pool['token1']}")
    print(f"Fee tier: {pool['fee']}%")
    print(f"TVL: ${pool['tvl_usd']:,.0f}")
    print("Analysis pipeline ready for extension.")


if __name__ == "__main__":
    main()
