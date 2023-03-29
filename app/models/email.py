from typing import Dict

from app.core import VDB

from dotenv import load_dotenv

load_dotenv()


class Email:
    schema_name = "Email"

    _fail_resp = {"status": "failure"}

    def get_emails(self, concepts, row_count=2) -> Dict:
        db = VDB().connect()

        nearText = {
            "concepts": [concepts],
        }

        search_headers = ["email_id", "send_date", "em_to", "subject", "content"]
        print(nearText)
        result = (
            db.client.query.get(self.schema_name, search_headers)
            .with_near_text(nearText)
            .with_limit(row_count)
            .do()
        )

        email_data = result["data"]["Get"]["Email"]

        output = {"result": email_data, "status": "success"}
        return output
