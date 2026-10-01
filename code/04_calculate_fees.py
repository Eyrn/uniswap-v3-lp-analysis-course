#!/usr/bin/env python3
"""Compute a simple fee accrual estimate for a Uniswap V3 position."""

import json
from pathlib import Path


def load_position_data(path: str | None = None):
    default_path = Path(__file__).resolve().parents[1] / "data" / "sample_positions.json"
    target = Path(path) if path else default_path
    with target.open("r", encoding="utf-8") as f:
        return json.load(f)


def estimate_fee_accrual(position, fee_rate: float = 0.003):
    # Approximate fee revenue = USD liquidity * fee rate * time factor
    # Here we use a small, illustrative scalar to keep the example easy to understand.
    return position["liquidity"] * fee_rate * 0.0025


def main():
    positions = load_position_data()
    print("=== Fee Estimation ===")
    for pos in positions:
        est = estimate_fee_accrual(pos)
        print(f"Position {pos['position_id']}: estimated fee = ${est:,.2f} USD")


if __name__ == "__main__":
    main()
