import base64
from auth import authenticate_user


def list_messages(service,user_id="me",max_results=200):
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
