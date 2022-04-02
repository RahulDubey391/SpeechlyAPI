from google.cloud import storage

class StoreCon:
    def get_con(self,bucket_name):
        client = storage.Client()
        bucket = client.get_bucket(bucket_name)
        return bucket