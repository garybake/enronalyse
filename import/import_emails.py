import email
import os
import glob
from html.parser import HTMLParser

from dotenv import load_dotenv
load_dotenv()

def parse_single_email(filename):
    with open(filename) as f:
        em = email.message_from_file(f)

    class HTMLFilter(HTMLParser):
        text = ""

        def handle_data(self, data):
            self.text += data

    payload = em.get_payload(decode=True)
    f = HTMLFilter()
    f.feed(payload.decode())
    content = f.text

    em_to = None
    if em["cc"]:
        em_to = [x.strip() for x in em["cc"].split(",")]

    em_cc = None
    if em["cc"]:
        em_cc = [x.strip() for x in em["cc"].split(",")]

    return {
        # "content_type": em.get_content_type(),
        "send_date": em["date"].strip(),
        "em_from": em["from"].strip(),
        "em_to": em_to,
        "em_cc": em_cc,
        "subject": em["subject"].strip(),
        "content": content
    }


def parse_email_folder(email_folder, max_parse=None):

    emails = []
    parse_count = 0

    for filepath in glob.glob(email_folder, recursive=True):
        print(filepath)
        em = parse_single_email(filepath)
        emails.append(em)
        parse_count += 1
        if max_parse and parse_count >= max_parse:
            break

    return emails


def main():
    email_folder = os.getenv("EMAIL_FOLDER")
    emails = parse_email_folder(email_folder, max_parse=10)
    print(len(emails))
    # print(emails[0])


if __name__ == "__main__":
    main()
