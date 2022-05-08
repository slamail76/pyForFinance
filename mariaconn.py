# Module Import
import mariadb as db
import sys

# Print List of Contacts
def ticker_select(cur):
    """Retrieves the list of contacts from the database and prints to stdout"""

    # Initialize Variables
    tickers_list = []

    # Retrieve Contacts
    cur.execute("SELECT Ticker, Company FROM tickers")
    i = 0
    # Prepare Contacts
    for (ticker, company) in cur:
         #tickers_list.append(f"{ticker} {company}")
         i += 1
         print(f"Il {i} ticker è {ticker} {company}")



# Instantiate Connection
try:
   conn = db.connect(
      user="root",
      password="stefano",
      host="192.168.15.194",
      database="pyfinance",
      port=3306)

   # Instantiate Cursor
   cur = conn.cursor()

   # Call function to print contacts
   ticker_select(cur)

   # Close Connection
   conn.close()

except db.Error as e:
       print(f"Error connecting to MariaDB Enterprise, or running DML : {e}")
       sys.exit(1)