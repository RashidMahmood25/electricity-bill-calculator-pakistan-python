# Electricity Bill Calculator — Pakistan (Python)
A small command-line estimator for a residential electricity bill's energy charge, calculated slab by slab.
## How to run
python3 electricity_bill_calculator.py
Enter the units (kWh) consumed and it prints the slab breakdown, the estimated energy charge, and the average cost per unit.
## Slab / estimate note (important)
The slab rates in the script are illustrative placeholder rates, not the current notified tariff of any DISCO. Real bills also add fixed charges, fuel price adjustment (FPA), GST and other surcharges, which this tool does not include. Treat the result as an estimate, and check your DISCO's latest tariff for an exact figure. The slab table is easy to edit at the top of the script (SLABS).
## What was practiced
- Slab-wise (tiered) pricing calculation
- Clean breakdown output so the user can verify each slab
- Labelling estimates vs official figures honestly
