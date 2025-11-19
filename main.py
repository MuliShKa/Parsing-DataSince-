import json
import statistics

with open("applied_atat.json", "r", encoding="utf-8") as f:
    data = json.load(f)

count = sum(len(region["values"]) for region in data["data"])
print("Количество k-values:", count)




regions = data["data"]


all_values = []

for region in regions:
    name = region["title_en"]
    values = [v["value"] for v in region["values"]]
    years = [v["key"] for v in region["values"]]

    avg_val = round(statistics.mean(values), 2)
    min_val = min(values)
    max_val = max(values)
    diff = values[0] - values[-1] 
    trend = "increase" if diff > 0 else "decrease"

    print(f"{name}:")
    print(f"  Min: {min_val}")
    print(f"  Max: {max_val}")
    print(f"  Average: {avg_val}")
    print(f"  Change 2014→2018: {diff} ({trend})\n")

    all_values.extend(values)


print(f" average: {round(statistics.mean(all_values), 2)}")
print(f"minimum: {min(all_values)}")
print(f" maximum: {max(all_values)}")  

