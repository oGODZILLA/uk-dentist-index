import json
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.nhs.uk/service-search/find-a-dentist/results/{}?distance=15"

def scrape_page(page):
    url = BASE_URL.format(page)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    results = soup.select(".nhsuk-card")

    dentists = []

    for card in results:
        name_el = card.select_one(".nhsuk-card__heading")
        desc_el = card.select_one(".nhsuk-card__description")
        link_el = card.select_one("a")

        if not name_el or not desc_el or not link_el:
            continue

        name = name_el.get_text(strip=True)
        address = desc_el.get_text(" ", strip=True)
        link = link_el["href"]
        website = "https://www.nhs.uk" + link

        dentists.append({
            "name": name,
            "address": address,
            "website": website
        })

    return dentists

def main():
    all_dentists = []

    for page in range(1, 20):  # scrape first 20 pages
        print("Scraping page:", page)
        dentists = scrape_page(page)
        all_dentists.extend(dentists)

    with open("dentists_raw.json", "w") as f:
        json.dump(all_dentists, f, indent=4)

    print("Saved dentists_raw.json with", len(all_dentists), "records")

if __name__ == "__main__":
    main()
