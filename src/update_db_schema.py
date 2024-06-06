from db import DBO

class UpdateDBSchema(DBO):
    ALTER_COUNTRY_ADD_TLD = "ALTER TABLE country ADD COLUMN topLevelDomain TEXT;"
    ALTER_COUNTRY_ADD_CAPITAL = "ALTER TABLE country ADD COLUMN capital TEXT;"

    def run(self):
        try:
            self.cursor.execute(self.ALTER_COUNTRY_ADD_TLD)
        except Exception as e:
            print(f"Error adding topLevelDomain column: {e}")
        
        try:
            self.cursor.execute(self.ALTER_COUNTRY_ADD_CAPITAL)
        except Exception as e:
            print(f"Error adding capital column: {e}")
        self.conn.commit()
        print("Database schema updated successfully.")

if __name__ == "__main__":
    UpdateDBSchema().run()
