import os

import weaviate

from dotenv import load_dotenv

load_dotenv()


class VDB:
    def __init__(self) -> None:
        self.db_url = os.getenv("VDB_URL")

    def connect(self):
        api_key = os.getenv("OPENAI_API_KEY")

        self.client = weaviate.Client(
            url=self.db_url, additional_headers={"X-OpenAI-Api-Key": api_key}
        )
        return self
