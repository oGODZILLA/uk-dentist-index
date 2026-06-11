import json

def main():
    # Load raw data
    with open("dentists_raw.json", "r") as f:
        data = json.load(f)

    cleaned = []

    for d in data:
        cleaned.append({
            "name": d.get("name", "").strip(),
            "address": d.get("address", "").strip(),
            "website": d.get("website", "").strip()
        })

    # Save cleaned data
    with open("dentists_clean.json", "w") as f:
        json.dump(cleaned, f, indent=4)

    print("Saved dentists_clean.json with", len(cleaned), "records")

if __name__ == "__main__":
    main()
