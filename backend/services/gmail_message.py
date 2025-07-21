import base64
from services.auth import authenticate_user
from services.scraper import extract_unsubscribe_links


def list_messages(service,user_id="me",max_results=40):
  response = service.users().messages().list(
    userId = user_id,
    maxResults = max_results
    ).execute()

  message = response.get("messages", [])
  return message

def get_html_from_message(service,message_id,user_id="me"):
  message_content = service.users().messages().get(
    id= message_id,
    userId = user_id,
    format = 'full'
    ).execute()
  
  payload = message_content.get('payload', {})
  parts = payload.get('parts', [])
  
  for part in parts:
    if part.get('mimeType') == 'text/html':
      html_data = part['body']['data']
      return base64.urlsafe_b64decode(html_data).decode('utf-8')
  return None

def list_messages_with_links(service,user_id="me"):
  
  #Get basic messages using existing function
  unfiltered_messages = list_messages(service,user_id=user_id,max_results=40)

  messages_with_links = []

  for msg in unfiltered_messages:
    msg_id = msg.get("id")
    html = get_html_from_message(service,msg_id,user_id=user_id)
    links = extract_unsubscribe_links(html) if html else []
    if links:
      msg["unsubscribe_links"] = links
      messages_with_links.append(msg)
  return messages_with_links
