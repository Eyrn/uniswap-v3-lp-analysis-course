#!/usr/bin/env python3
"""Simplified position parser for a sample Uniswap V3 position."""

import json
from pathlib import Path


def load_position_data(path: str | None = None):
    default_path = Path(__file__).resolve().parents[1] / "data" / "sample_positions.json"
    target = Path(path) if path else default_path
    with target.open("r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def main():
    positions = load_position_data()
    print("=== Position Summary ===")
    for pos in positions:
        print(f"Position ID: {pos['position_id']}")
        print(f"  Pool: {pos['pool_address']}")
        print(f"  Range: [{pos['lower_tick']}, {pos['upper_tick']}]")
        print(f"  Liquidity: {pos['liquidity']}")
        print(f"  Token0 Amount: {pos['token0_amount']}")
        print(f"  Token1 Amount: {pos['token1_amount']}")
        print(f"  Fee Accrued: ${pos['fees_accrued_usd']:.2f}")
        print()


if __name__ == "__main__":
    main()
