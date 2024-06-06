import json
from db import DBO

class RegionStats(DBO):
    def get_stats(self):
        query = """
            SELECT r.name AS region_name, COUNT(c.id) AS number_countries, SUM(c.population) AS total_population
            FROM region r
            LEFT JOIN country c ON r.id = c.region_id
            GROUP BY r.name;
        """
        self.cursor.execute(query)
        regions_data = self.cursor.fetchall()
        headers = [header[0] for header in self.cursor.description]
        regions = [{k: v for k, v in zip(headers, row)} for row in regions_data]
        return {"regions": regions}

    def run(self):
        stats = self.get_stats()
        print(json.dumps(stats, indent=4))

if __name__ == "__main__":
    RegionStats().run()
