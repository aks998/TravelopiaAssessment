import psycopg2

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

def load_data_into_postgres(connection):
    if connection is None:
        return

    try:
        cursor = connection.cursor()

        with open("customer_data.csv", "r") as f:
            cursor.copy_expert("COPY customer_data FROM STDIN CSV HEADER", f)
        
        with open("booking_data.csv", "r") as f:
            cursor.copy_expert("COPY booking_data FROM STDIN CSV HEADER", f)
        
        with open("destination_data.csv", "r") as f:
            cursor.copy_expert("COPY destination_data FROM STDIN CSV HEADER", f)

        connection.commit()

        print("Data loaded into PostgreSQL successfully.")
    except psycopg2.Error as e:
        print("Error loading data into PostgreSQL:", e)


# Establishing Connection and then loading transformed data to PostgreSQL
connection = create_connection()
if connection is not None:
    load_data_into_postgres(connection)
