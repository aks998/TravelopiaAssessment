import schedule
import time
import psycopg2
from google.cloud import storage

def create_connection():
    try:
        connection = psycopg2.connect(
            host="localhost",
            database = "postgres",
            user="postgres",
            password="12345678"
        )
        print("Connection Successfull")
        return connection
    except psycopg2.Error as e:
        print("Error connecting to the PostgreSQL database:", e)
        return None

def aggregate_data(connection):
    
    cursor = connection.cursor()
    query = '''
        SELECT destination, COUNT(booking_id) as total_bookings
        FROM booking_data
        GROUP BY destination
    '''

    cursor.execute(query)
    results = cursor.fetchall()

    storage_client = storage.Client()

    csv_data = "destination,total_bookings\n"
    for row in results:
        csv_data += f"{row[0]},{row[1]}\n"

    bucket = storage_client.bucket("myBucket")
    blob = bucket.blob('total_bookings_per_destination.csv')
    blob.upload_from_string(csv_data)
    cursor.close()
    print('Data aggregation complete.')

connection = create_connection()
schedule.every().hour.do(aggregate_data, connection=connection)

while True:
    schedule.run_pending()
    time.sleep(1)
