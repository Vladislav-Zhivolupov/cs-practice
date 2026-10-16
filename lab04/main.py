#main

import sys
from stats import average_by_city, read_valid, warmest_city
 
 
def main() -> None:
    lines = sys.stdin.read().splitlines()
    records = read_valid(lines)
    non_empty = sum(1 for line in lines if line.strip())
    skipped = non_empty - len(records)
 
    print(len(records))
    print(skipped)
    if records:
        best = warmest_city(records)
        print(f"{average_by_city(records)[best]:.1f}")
    else:
        print(f"{0:.1f}")
 
 
if __name__ == "__main__":
    main()
