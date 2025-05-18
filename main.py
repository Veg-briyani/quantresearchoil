import argparse
from core.gann.calculator import GannCalculator
from core.time.cycles import OilCycles

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--timeframe', default='4h')
    parser.add_argument('--phase', type=int, default=3)
    args = parser.parse_args()

    print(f"Running Gann Oil Trader on {args.timeframe} timeframe...")
    
    # Initialize core components
    gann = GannCalculator()
    cycles = OilCycles()
    
    # TODO: Add data loading and processing

if __name__ == "__main__":
    main()