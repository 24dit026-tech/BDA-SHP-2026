import sys

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    year, temperature = line.split(",")

    print(f"{year}\t{temperature}")
