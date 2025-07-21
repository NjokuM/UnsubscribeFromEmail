import base64
from services.auth import authenticate_user
from services.scraper import extract_unsubscribe_links


def list_messages(service, includeSpamTrash=True, user_id="me", max_results=40):
    response = service.users().messages().list(
        userId=user_id,
        maxResults=max_results,
        includeSpamTrash=includeSpamTrash
    ).execute()

    return response.get("messages", [])


def get_full_message(service, message_id, user_id="me"):
    return service.users().messages().get(
        id=message_id,
        userId=user_id,
        format='full'
    ).execute()


def parse_headers(headers):
    sender = subject = None
    for header in headers:
        name = header.get("name")
        if name == "From":
            raw_sender = header.get("value")
            sender = extract_sender_name(raw_sender)
        elif name == "Subject":
            subject = header.get("value")
    return sender, subject

def extract_sender_name(sender_raw):
    if '<' in sender_raw:
        name_part = sender_raw.split('<')[0].strip()
        if name_part:  # checks if there's anything before the '<'
            return name_part
    return sender_raw



def extract_html_from_payload(payload):
    parts = payload.get("parts", [])
    for part in parts:
        if part.get("mimeType") == "text/html":
            html_encoded = part.get("body", {}).get("data")
            if html_encoded:
                return base64.urlsafe_b64decode(html_encoded).decode("utf-8")
    return None


def list_messages_with_links(service, user_id="me", max_results=100):
    messages = list_messages(service, user_id=user_id, max_results=max_results)
    messages_with_links = []

    for msg in messages:
        msg_id = msg.get("id")
        message = get_full_message(service, msg_id, user_id=user_id)

        payload = message.get("payload", {})
        headers = payload.get("headers", [])

        sender, subject = parse_headers(headers)
        html_body = extract_html_from_payload(payload)

        unsubscribe_links = extract_unsubscribe_links(html_body) if html_body else []

        if unsubscribe_links:
            messages_with_links.append({
                "id": msg_id,
                "from": sender,
                "subject": subject,
                "unsubscribe_links": unsubscribe_links
            })

    return messages_with_links
