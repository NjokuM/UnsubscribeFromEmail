from fastapi import APIRouter, HTTPException
from services.gmail_message import list_messages
from services.auth import authenticate_user

router = APIRouter()

@router.get("/messages")
def get_gmail_messages():
  try:
    service = authenticate_user()
    if not service:
      raise HTTPException(status_code=401, detail="Failed to authenticate with Gmail")
    
    messages = list_messages(service)
    return {"message_count" : len(messages), "messages" : messages}
  
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
  
