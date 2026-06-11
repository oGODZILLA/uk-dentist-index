import json
import requests

SUPABASE_URL = "https://jbafdmwjnyybbaxndbke.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImpiYWZkbXdqbnl5YmJheG5kYmtlIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc4MTA4NDc3MCwiZXhwIjoyMDk2NjYwNzcwfQ.RY8Cgr7ohEWjKalF7qrnn5ehKPlPQ2YugA_QC82HmOc"

def main():
    with open("dentists_enriched.json", "r") as f:
        data = json.load(f)

    url = f"{SUPABASE_URL}/rest/v1/dentists"

    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=minimal"
    }

    for i, d in enumerate(data, start=1):
        payload = {
            "name": d["name"],
            "address": d["address"],
            "website": d["website"],
            "data": d
        }

        r = requests.post(url, headers=headers, json=payload)

        if r.status_code not in (200, 201, 204):
            print(f"Error uploading record {i}: {r.text}")
        else:
            print(f"Uploaded {i}/{len(data)}")

    print("Upload complete.")

if __name__ == "__main__":
    main()
