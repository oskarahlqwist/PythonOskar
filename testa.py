from dataclasses import dataclass

@dataclass
class Position:
    name: str
    lon: float
    lat: float

t = Position("Oskar", 20.32, 23.55)

print(f'{t.name} is at {t.lat}°N, {t.lon}°E')