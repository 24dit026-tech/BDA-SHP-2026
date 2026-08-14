import sys

current_year = None
maximum_temperature = None

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    year, temperature = line.split("\t")
    temperature = int(temperature)

    if current_year == year:
        maximum_temperature = max(maximum_temperature, temperature)
    else:
        if current_year is not None:
            print(f"{current_year}\t{maximum_temperature}")

        current_year = year
        maximum_temperature = temperature

if current_year is not None:
    print(f"{current_year}\t{maximum_temperature}")
