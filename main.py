"""Charm the Commuter entry: one line of weather forecast for a city
that does not exist, written to /output/entry.txt (the comp contract).
Deterministic: the same line, byte for byte, on every run."""
import os

LINE = "Good morning, Breathton: minus 4°, frost on the platform — your breath fogs the bus windows, where the driver has drawn you a sunny day."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
