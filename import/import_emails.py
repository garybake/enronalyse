import os
import json

import weaviate
from dotenv import load_dotenv

from read_emails import get_email_data, get_email_from_pickle

load_dotenv()


class VDB:
    def __init__(self):
        self.client = None

    def connect(self):
        db_url = os.getenv("VDB_URL")
        api_key = os.getenv("OPENAI_API_KEY")

        self.client = weaviate.Client(
            url=db_url, additional_headers={"X-OpenAI-Api-Key": api_key}
        )
        return self


class EmailData:
    def create_schema(self):
        class_obj = {
            "class": "Email",
            "vectorizer": "text2vec-openai",  # "text2vec-huggingface",  # "text2vec-transformers"
        }

        db = VDB().connect()
        db.client.schema.delete_class("Email")  # uncomment to delete table if needed
        db.client.schema.create_class(class_obj)

    def insert_emails(self, email_data):
        db = VDB().connect()

        with db.client.batch as batch:
            batch.batch_size = 50
            sent = 0
            for email in email_data:
                db.client.batch.add_data_object(email, "Email")
                sent += 1
                if sent % 100 == 0:
                    print(f"Uploaded {sent} messages")

    def query(self, query_term, row_count=2):
        db = VDB().connect()

        search_headers = ["email_id", "send_date", "em_to", "subject", "content"]

        nearText = {
            "concepts": [query_term],
        }

        result = (
            db.client.query.get("Email", search_headers)
            .with_near_text(nearText)
            .with_limit(row_count)
            .do()
        )

        return result


if __name__ == "__main__":
    eup = EmailData()
    
    # eup.create_schema()

    # email_data = get_email_data(max_emails=500)
    # email_data = get_email_from_pickle(max_emails=2)
    # eup.insert_emails(email_data)

    # result = eup.query("the captain of the titanic")
    # print(json.dumps(result, indent=4))
