# Connessione al db maria
import mariadb as db
import sys


# Print List of Contacts
def urladdress(regione, settore):
    reg = str(regione)
    sect = str(settore)
    try:
        conn = db.connect(
            user="root",
            password="stefano",
            host="192.168.15.194",
            database="pyfinance",
            port=3306)

        # Instantiate Cursor
        cur = conn.cursor()

        # Retrieve Contacts
        cur.execute("SELECT url, limite FROM t_url WHERE Region=%s AND Sector=%s", (reg, sect))

        # Prepare Contacts
        for (url) in cur:
            return url
        conn.close()

    except db.Error as e:
        print(f"Error connecting to MariaDB Enterprise, or running DML : {e}")
        sys.exit(1)
