
class Building:
    total = 0

    def __init__(self):
        Building.total += 1


buildings = [Building() for _ in range(40)]


for idx, building in enumerate(buildings, 1):
    print(f"Здание {idx}: {building}")

print(f"Всего создано зданий: {Building.total}")