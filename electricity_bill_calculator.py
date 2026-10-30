#!/usr/bin/env python3
"""Electricity bill estimator for Pakistan (residential, educational).
Uses a simplified slab structure the user can see and edit. Real
DISCO bills also include fixed charges, fuel price adjustment (FPA),
taxes/surcharges and slab changes that vary by distributor and month,
so this is an ESTIMATE of the energy charge only, not a replica bill.
Default slabs (PKR per unit, editable in SLABS below):
  0-100 units:   22.00
  101-200:       28.00
  201-300:       34.00
  301-400:       40.00
  401-500:       44.00
  501-600:       46.00
  601-700:       48.00
  701+:          50.00
These are PLACEHOLDER/illustrative rates, not the current notified
tariff. Check your DISCO's latest tariff before relying on the figure.
"""
SLABS = [
    (100, 22.00),
    (200, 28.00),
    (300, 34.00),
    (400, 40.00),
    (500, 44.00),
    (600, 46.00),
    (700, 48.00),
    (float("inf"), 50.00),
]
def energy_charge(units):
    remaining = units
    previous_limit = 0
    total = 0.0
    breakdown = []
    for limit, rate in SLABS:
        if remaining <= 0:
            break
        slab_units = min(remaining, limit - previous_limit)
        cost = slab_units * rate
        breakdown.append((previous_limit + 1, previous_limit + slab_units, rate, cost))
        total += cost
        remaining -= slab_units
        previous_limit = limit
    return total, breakdown
def main():
    print("=== Electricity Bill Estimator (Pakistan, residential) ===")
    print("Estimates the ENERGY CHARGE only — taxes, FPA and fixed")
    print("charges are NOT included. Rates below are illustrative.\n")
    while True:
        try:
            units = float(input("Units consumed (kWh): ").strip())
            if units < 0:
                print("  Please enter 0 or a positive number.")
                continue
            break
        except ValueError:
            print("  Please enter a number.")
    total, breakdown = energy_charge(units)
    print("\n--- Slab breakdown ---")
    for start, end, rate, cost in breakdown:
        end_label = int(end) if float(end).is_integer() else end
        label = f"{start}-{end_label}" if start != end else f"{start}"
        print(f"  {label} units @ PKR {rate:.2f} = PKR {cost:,.2f}")
    print(f"\nEstimated energy charge: PKR {total:,.2f}")
    print("Average per unit: PKR {:.2f}".format(total / units if units else 0))
    print("\nNote: add your DISCO's fixed charges, FPA, GST and other")
    print("surcharges for a bill closer to the real one.")
if __name__ == "__main__":
    main()
