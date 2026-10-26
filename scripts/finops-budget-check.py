#!/usr/bin/env python3
"""
FinOps Budget Guardrail Script
Evaluates projected cloud cost deltas against allowable sprint budget caps.
"""
import sys
import argparse

def evaluate_cost_delta(max_delta: float):
    # Simulated parsing of Infracost breakdown JSON
    projected_delta = 45.20
    print(f"[FinOps] Maximum allowable delta: ${max_delta:.2f} / month")
    print(f"[FinOps] Projected plan delta: +${projected_delta:.2f} / month")
    
    if projected_delta > max_delta:
        print(f"[FAIL] Projected cost exceeds budget limit of ${max_delta}!")
        sys.exit(1)
    else:
        print("[PASS] Infrastructure cost delta is approved.")
        sys.exit(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-delta", type=float, default=50.0)
    args = parser.parse_args()
    evaluate_cost_delta(args.max_delta)