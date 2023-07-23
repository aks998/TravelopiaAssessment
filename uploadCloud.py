from google.cloud import storage

def upload_to_gcp():
    file = ["customer_data.csv", "booking_data.csv", "destination_data.csv"]
    bucket = "myBucket"
    storage_client = storage.Client()
    for i in range(3):
        bucket = storage_client.bucket(bucket)
        blob = bucket.blob(file[i])
        blob.upload_from_filename(file[i])

upload_to_gcp()