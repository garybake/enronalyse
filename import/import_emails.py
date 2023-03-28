import os

import weaviate

from read_emails import get_email_data

from dotenv import load_dotenv

load_dotenv()


class VDB:
    def __init__(self):
        self.client = None

    def connect(self):
        db_url = os.getenv("VDB_URL")
        api_key = os.getenv("HUGGINGFACE_API_KEY")

        self.client = weaviate.Client(
            url=db_url,
            additional_headers = {
                "X-HuggingFace-Api-Key": api_key
            }
        )
        return self


class EmailUploader:

    def create_schema(self):
        class_obj = {
            "class": "Email",
            "vectorizer": "text2vec-huggingface"  # "text2vec-transformers"
        }

        db = VDB().connect()
        # db.client.schema.delete_class("Email")  # uncomment to delete table if needed
        db.client.schema.create_class(class_obj)

    def insert_emails(self, email_data):
        db = VDB().connect()

        with db.client.batch as batch:
            batch.batch_size=50
            for email in email_data:
                db.client.batch.add_data_object(email, "Email")

if __name__ == "__main__":
    eup = EmailUploader()
    # eup.create_schema()

    email_data = get_email_data(max_emails=20)
    eup.insert_emails(email_data)
    print(len(email_data))
    # print(email_data[0])
