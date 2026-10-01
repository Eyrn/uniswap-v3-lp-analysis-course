#!/usr/bin/env python3
"""Estimate impermanent loss (IL) from a price move."""

import math


def calculate_il(price_before: float, price_after: float) -> float:
    """Return IL as a percentage, using a simplified formula.

    For a 50/50 LP, IL around price move is:
      IL = 1 - (2 * sqrt(P)) / (1 + P)
    where P is price_after / price_before.
    """
    ratio = price_after / price_before
    if ratio <= 0:
        raise ValueError("Price ratio must be positive.")
    return 1 - (2 * math.sqrt(ratio) / (1 + ratio))


def main():
    scenarios = [
        (1.0, 0.8),
        (1.0, 1.0),
        (1.0, 1.5),
        (1.0, 2.0),
        (1.0, 3.0),
    ]
    print("=== Impermanent Loss by Price Move ===")
    for before, after in scenarios:
        il = calculate_il(before, after)
        print(f"Price {before} -> {after}: IL = {il * 100:.2f}%")


if __name__ == "__main__":
    main()
