#!/usr/bin/env python3
"""Combine fee revenue and impermanent loss to estimate net LP profit."""


def net_profit(fee_usd: float, il_usd: float) -> float:
    return fee_usd - abs(il_usd)


def main():
    results = [
        {"fee_usd": 1200, "il_usd": 450},
        {"fee_usd": 1500, "il_usd": 1200},
        {"fee_usd": 900, "il_usd": 200},
    ]
    print("=== Net Profit Estimate ===")
    for item in results:
        profit = net_profit(item["fee_usd"], item["il_usd"])
        print(f"Fee: ${item['fee_usd']}; IL: ${item['il_usd']}; Net: ${profit}")


if __name__ == "__main__":
    main()
