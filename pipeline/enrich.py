import json

def main():
    # Load signals data
    with open("dentists_signals.json", "r") as f:
        data = json.load(f)

    enriched = []

    for d in data:
        website = d.get("website", "").lower()

        # Example enrichment rules
        has_https = website.startswith("https://")
        has_custom_domain = not website.endswith(".nhs.uk") if website else False
        is_missing_website = website == ""

        enriched.append({
            "name": d["name"],
            "address": d["address"],
            "website": d["website"],
            "signals": d["signals"],
            "enrichment": {
                "has_https": has_https,
                "has_custom_domain": has_custom_domain,
                "is_missing_website": is_missing_website
            }
        })

    # Save enriched file
    with open("dentists_enriched.json", "w") as f:
        json.dump(enriched, f, indent=4)

    print("Saved dentists_enriched.json with", len(enriched), "records")

if __name__ == "__main__":
    main()
