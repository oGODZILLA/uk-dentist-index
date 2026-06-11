import json

def main():
    # Load cleaned data
    with open("dentists_clean.json", "r") as f:
        data = json.load(f)

    enriched = []

    for d in data:
        name = d.get("name", "").lower()
        address = d.get("address", "").lower()

        # Simple example signals
        has_nhs = "nhs" in name or "nhs" in address
        has_dental = "dental" in name
        long_address = len(address) > 40

        enriched.append({
            "name": d["name"],
            "address": d["address"],
            "website": d["website"],
            "signals": {
                "has_nhs": has_nhs,
                "has_dental": has_dental,
                "long_address": long_address
            }
        })

    # Save signals file
    with open("dentists_signals.json", "w") as f:
        json.dump(enriched, f, indent=4)

    print("Saved dentists_signals.json with", len(enriched), "records")

if __name__ == "__main__":
    main()

