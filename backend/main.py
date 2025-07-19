from auth import authenticate_user
from gmail_message import list_messages, get_html_from_message
from scraper import extract_unsubscribe_links

def main():
    service = authenticate_user()

    if not service:
        print ("Failed to authenticate")
        return
    
    print("Fetching Messages...")
    messages = list_messages(service)

    print(f"Found {len(messages)} messages. Scanning for unsubscribe links ... \n")

    for msg in messages: 
      msg_id = msg["id"]
      html = get_html_from_message(service, msg_id)

      if html:
        links = extract_unsubscribe_links(html)
        if links:
          print(f"\nMessage ID : {msg_id} ")
          for link in links:
             print(f"  ↳ {link}")
      else:
         print(f"Message ID: {msg_id} - No html content. ")

if __name__ == "__main__":
   main()