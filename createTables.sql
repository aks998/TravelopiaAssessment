CREATE TABLE customer_data (
    customer_id INTEGER PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(100) NOT NULL
)

CREATE TABLE booking_data (
    booking_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    booking_date DATE NOT NULL,
    destination VARCHAR(100) NOT NULL,
    number_of_passengers INTEGER NOT NULL,
    cost_per_passenger INTEGER NOT NULL,
    total_booking_value INTEGER NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customer_data (customer_id)
)

CREATE TABLE destination_data (
    destination_id INTEGER PRIMARY KEY,
    destination VARCHAR(100) NOT NULL,
    country VARCHAR(50) NOT NULL,
    popular_season VARCHAR(10) NOT NULL
)