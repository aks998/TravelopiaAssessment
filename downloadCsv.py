import requests
import pandas as pd
import csv

# 1st Part Downloading the CSV files from GITHUB.

def download_csv():
    url = ["https://github.com/aks998/CSV_FILES/blob/main/booking_data.csv?raw=true" , 
                      "https://github.com/aks998/CSV_FILES/blob/main/customer_data.csv?raw=true" ,
                      "https://github.com/aks998/CSV_FILES/blob/main/destination_data.csv?raw=true"
    ]
    file_name = ["booking_data.csv" , "customer_data.csv" , "destination_data.csv"]

    for i in range(3) :
        response = requests.get(url[i])
        with open(file_name[i], 'wb') as file:
            file.write(response.content)



# 2nd Part Cleansing and Transforming Data

def cleanse_and_transform():
    customer_df = pd.read_csv("customer_data.csv" , quoting = csv.QUOTE_ALL).astype(str)
    booking_df = pd.read_csv("booking_data.csv" , quoting=csv.QUOTE_ALL).astype(str)
    destination_df = pd.read_csv("destination_data.csv", quoting=csv.QUOTE_ALL).astype(str)
    
    # Handling Erroneous Data
    customer_df.fillna("N/A", inplace=True)
    booking_df.fillna("N/A", inplace=True)
    destination_df.fillna("N/A" , inplace=True)
    
    booking_df = booking_df.astype({"number_of_passengers" : "int" , "cost_per_passenger" : "int"})
    
    # Convert date format
    booking_df["booking_date"] = pd.to_datetime(booking_df["booking_date"], format="%Y-%m-%d")
    
    # Adding total_booking_value
    booking_df["total_booking_value"] = booking_df["number_of_passengers"] *  booking_df["cost_per_passenger"]
    booking_df["total_booking_value"] = booking_df["total_booking_value"].astype(int)
    

    customer_df = customer_df.astype(str)
    booking_df = booking_df.astype(str)
    destination_df = destination_df.astype(str)

    customer_df.replace("nan" , "")
    booking_df.replace("nan" , "")
    destination_df.replace("nan" , "")

    customer_df.to_csv("customer_data.csv" , index = False , quoting=csv.QUOTE_ALL)
    booking_df.to_csv("booking_data.csv" , index = False , quoting=csv.QUOTE_ALL)
    destination_df.to_csv("destination_data.csv" , index = False , quoting=csv.QUOTE_ALL)


download_csv()
cleanse_and_transform()