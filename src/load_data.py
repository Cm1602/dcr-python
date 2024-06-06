import requests
from db import Country, Region


class LoadData:
    DATA_URL = "https://storage.googleapis.com/dcr-django-test/countries.json"

    def __init__(self):
        # Cache of regions
        self.regions = {}

    def get_raw_data(self):
        response = requests.get(self.DATA_URL)
        response.raise_for_status() 
        print(response.json())
        return response.json()

    def add_country(self, data):
        region_name = data.get("region", "Unknown")
        region_id = self.get_region_id(region_name)

        country = Country()
        found = country.get_by_name(data["name"])
        print(found)
        if found:
            return
        
        topLevelDomain = data.get("topLevelDomain")
        if isinstance(topLevelDomain, list):
            topLevelDomain = ','.join(topLevelDomain)
            
        country.insert(
            data.get("name"),
            data.get("alpha2Code"),
            data.get("alpha3Code"),
            data.get("population"),
            region_id,
            topLevelDomain,
            data.get("capital"),
        )
        print(country.data)

    def get_region_id(self, region_name):
        if region_name not in self.regions:
            region = Region()
            region.get_or_create_by_name(region_name)
            self.regions[region.data["name"]] = region.data["id"]
        return self.regions[region_name]

    def run(self):
        data = self.get_raw_data()
        for row in data:
            self.add_country(row)


if __name__ == "__main__":
    LoadData().run()
